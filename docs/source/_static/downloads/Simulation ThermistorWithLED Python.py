import tkinter as tk
import time
import matplotlib.pyplot as plt


# ============================================================
# Simulation Configuration
# ============================================================
ROOM_TEMP_F = 70.0

# Temperature change during each 100 ms update
HEATING_RATE_F = 0.35
COOLING_RATE_F = 0.35

# Rate at which temperature returns toward room temperature
RETURN_RATE_F = 0.08

# Update the simulation every 100 milliseconds
UPDATE_INTERVAL_MS = 100

# Print to the serial-monitor-style terminal every 500 ms
SERIAL_PRINT_INTERVAL_SECONDS = 0.5


# ============================================================
# Terminal Threshold Input
# ============================================================
while True:
    try:
        HIGH_TEMP_F = float(
            input(
                "Enter the high temperature threshold in °F: "
            )
        )

        LOW_TEMP_F = float(
            input(
                "Enter the low temperature threshold in °F: "
            )
        )

        if LOW_TEMP_F >= HIGH_TEMP_F:
            print(
                "\nERROR: The low temperature threshold must "
                "be less than the high temperature threshold.\n"
            )
            continue

        break

    except ValueError:
        print(
            "\nERROR: Please enter valid numeric values, "
            "such as 85 or 70.5.\n"
        )


# ============================================================
# Simulation Variables
# ============================================================
temperature_f = ROOM_TEMP_F

heating = False
cooling = False
simulation_running = True
window_closing = False

elapsed_times = []
temperatures_c = []
temperatures_f = []

total_read = 0
last_serial_print_time = 0.0
start_time = 0.0

# Stores the ID of the scheduled Tkinter callback
after_id = None


# ============================================================
# Temperature Conversion
# ============================================================
def fahrenheit_to_celsius(temp_f):
    """Convert Fahrenheit to Celsius."""

    return (temp_f - 32.0) * 5.0 / 9.0


# ============================================================
# Button Functions
# ============================================================
def heat_press(event=None):
    """Start heating while the Heat Thermistor button is held."""

    global heating
    global cooling

    if not simulation_running:
        return

    heating = True
    cooling = False

    heat_button.config(
        relief="sunken",
        bg="#FFCCCC"
    )

    cool_button.config(
        relief="raised",
        bg="#F0F0F0"
    )


def heat_release(event=None):
    """Stop heating when the Heat Thermistor button is released."""

    global heating

    heating = False

    if not window_closing:
        heat_button.config(
            relief="raised",
            bg="#F0F0F0"
        )


def cool_press(event=None):
    """Start cooling while the Cool Thermistor button is held."""

    global heating
    global cooling

    if not simulation_running:
        return

    cooling = True
    heating = False

    cool_button.config(
        relief="sunken",
        bg="#CCE5FF"
    )

    heat_button.config(
        relief="raised",
        bg="#F0F0F0"
    )


def cool_release(event=None):
    """Stop cooling when the Cool Thermistor button is released."""

    global cooling

    cooling = False

    if not window_closing:
        cool_button.config(
            relief="raised",
            bg="#F0F0F0"
        )


def stop_heating_if_mouse_leaves(event=None):
    """Stop heating if the mouse leaves the Heat button."""

    heat_release()


def stop_cooling_if_mouse_leaves(event=None):
    """Stop cooling if the mouse leaves the Cool button."""

    cool_release()


# ============================================================
# Status and LED Logic
# ============================================================
def determine_temperature_state():
    """
    Determine the red LED, blue LED, and front-panel status.
    """

    red_led = temperature_f > HIGH_TEMP_F
    blue_led = temperature_f < LOW_TEMP_F

    if red_led:
        status_text = "OVERHEATING"
        status_background = "#F4B6B6"
        status_foreground = "#8B0000"

    elif blue_led:
        status_text = "TOO COLD"
        status_background = "#BFDDF5"
        status_foreground = "#003F7F"

    else:
        status_text = "IDEAL"
        status_background = "#BFE5BF"
        status_foreground = "#005A00"

    return (
        red_led,
        blue_led,
        status_text,
        status_background,
        status_foreground
    )


def update_front_panel():
    """Update the temperature, status, and LED indicators."""

    if window_closing:
        return

    (
        red_led,
        blue_led,
        status_text,
        status_background,
        status_foreground
    ) = determine_temperature_state()

    temperature_value.config(
        text=f"{temperature_f:.2f} °F"
    )

    celsius_value.config(
        text=f"{fahrenheit_to_celsius(temperature_f):.2f} °C"
    )

    status_value.config(
        text=status_text,
        bg=status_background,
        fg=status_foreground
    )

    # Red high-temperature LED
    if red_led:
        led_canvas.itemconfig(
            red_led_circle,
            fill="#E60000",
            outline="#990000"
        )
    else:
        led_canvas.itemconfig(
            red_led_circle,
            fill="#A0A0A0",
            outline="#606060"
        )

    # Blue low-temperature LED
    if blue_led:
        led_canvas.itemconfig(
            blue_led_circle,
            fill="#0066FF",
            outline="#003D99"
        )
    else:
        led_canvas.itemconfig(
            blue_led_circle,
            fill="#A0A0A0",
            outline="#606060"
        )


# ============================================================
# Serial-Monitor-Style Output
# ============================================================
def print_serial_monitor(temp_c, red_led, blue_led):
    """
    Print temperature and LED information to the terminal,
    similar to the original NI-DAQmx program.
    """

    red_status = "ON" if red_led else "OFF"
    blue_status = "ON" if blue_led else "OFF"

    print(
        f"Temperature: {temp_c:7.2f} °C | "
        f"{temperature_f:7.2f} °F | "
        f"Red LED: {red_status:3} | "
        f"Blue LED: {blue_status:3}"
    )


# ============================================================
# Main Simulation Loop
# ============================================================
def update_simulation():
    """Update the simulated thermistor and front panel."""

    global temperature_f
    global total_read
    global last_serial_print_time
    global after_id

    if not simulation_running or window_closing:
        return

    # Heat the simulated thermistor.
    if heating and not cooling:
        temperature_f += HEATING_RATE_F

    # Cool the simulated thermistor.
    elif cooling and not heating:
        temperature_f -= COOLING_RATE_F

    # Return slowly toward 70°F when neither button is pressed.
    else:
        if temperature_f > ROOM_TEMP_F:
            temperature_f -= min(
                RETURN_RATE_F,
                temperature_f - ROOM_TEMP_F
            )

        elif temperature_f < ROOM_TEMP_F:
            temperature_f += min(
                RETURN_RATE_F,
                ROOM_TEMP_F - temperature_f
            )

    temp_c = fahrenheit_to_celsius(
        temperature_f
    )

    elapsed_time = time.perf_counter() - start_time

    # Store every simulated reading for the final graph.
    elapsed_times.append(elapsed_time)
    temperatures_c.append(temp_c)
    temperatures_f.append(temperature_f)

    total_read += 1

    update_front_panel()

    red_led, blue_led, _, _, _ = (
        determine_temperature_state()
    )

    current_time = time.perf_counter()

    # Print at a slower interval so the terminal remains readable.
    if (
        current_time - last_serial_print_time
        >= SERIAL_PRINT_INTERVAL_SECONDS
    ):
        print_serial_monitor(
            temp_c,
            red_led,
            blue_led
        )

        last_serial_print_time = current_time

    # Schedule the next update and save the callback ID.
    after_id = root.after(
        UPDATE_INTERVAL_MS,
        update_simulation
    )


# ============================================================
# Close Simulation
# ============================================================
def close_simulation():
    """Stop the simulation and close the front panel cleanly."""

    global simulation_running
    global heating
    global cooling
    global window_closing
    global after_id

    # Prevent this function from running more than once.
    if window_closing:
        return

    window_closing = True
    simulation_running = False
    heating = False
    cooling = False

    # Cancel the pending update_simulation callback.
    if after_id is not None:
        try:
            root.after_cancel(after_id)
        except tk.TclError:
            pass

        after_id = None

    print("\nSimulation stopped by user.")
    print("Red LED: OFF")
    print("Blue LED: OFF")
    print(
        f"Acquired {total_read} total simulated readings."
    )

    root.quit()
    root.destroy()


# ============================================================
# Create Main Window
# ============================================================
root = tk.Tk()

root.title("Thermistor Simulation")
root.geometry("360x455")
root.resizable(False, False)

root.configure(
    bg="#E8E8E8"
)

root.protocol(
    "WM_DELETE_WINDOW",
    close_simulation
)


# ============================================================
# Front Panel Title
# ============================================================
title_label = tk.Label(
    root,
    text="Thermistor Simulation",
    font=("Arial", 17, "bold"),
    bg="#E8E8E8",
    fg="#202020"
)

title_label.pack(
    pady=(15, 10)
)


# ============================================================
# Threshold Summary
# ============================================================
threshold_label = tk.Label(
    root,
    text=(
        f"Low: {LOW_TEMP_F:.1f} °F    "
        f"High: {HIGH_TEMP_F:.1f} °F"
    ),
    font=("Arial", 9),
    bg="#E8E8E8",
    fg="#404040"
)

threshold_label.pack(
    pady=(0, 8)
)


# ============================================================
# Temperature Display
# ============================================================
temperature_frame = tk.Frame(
    root,
    bg="#E8E8E8"
)

temperature_frame.pack(
    pady=(0, 10)
)

temperature_label = tk.Label(
    temperature_frame,
    text="Temperature",
    font=("Arial", 10),
    bg="#E8E8E8",
    fg="#202020"
)

temperature_label.pack(
    anchor="w"
)

temperature_value = tk.Label(
    temperature_frame,
    text=f"{ROOM_TEMP_F:.2f} °F",
    width=17,
    height=1,
    font=("Arial", 14, "bold"),
    bg="#D3D3D3",
    fg="#202020",
    relief="sunken",
    bd=2
)

temperature_value.pack()

celsius_value = tk.Label(
    temperature_frame,
    text=f"{fahrenheit_to_celsius(ROOM_TEMP_F):.2f} °C",
    font=("Arial", 9),
    bg="#E8E8E8",
    fg="#505050"
)

celsius_value.pack(
    pady=(3, 0)
)


# ============================================================
# Status Display
# ============================================================
status_frame = tk.Frame(
    root,
    bg="#E8E8E8"
)

status_frame.pack(
    pady=(0, 8)
)

status_label = tk.Label(
    status_frame,
    text="Status",
    font=("Arial", 10),
    bg="#E8E8E8",
    fg="#202020"
)

status_label.pack(
    anchor="w"
)

status_value = tk.Label(
    status_frame,
    text="IDEAL",
    width=17,
    height=2,
    font=("Arial", 12, "bold"),
    bg="#BFE5BF",
    fg="#005A00",
    relief="sunken",
    bd=2
)

status_value.pack()


# ============================================================
# Simulated LED Indicators
# ============================================================
led_canvas = tk.Canvas(
    root,
    width=210,
    height=65,
    bg="#E8E8E8",
    highlightthickness=0
)

led_canvas.pack(
    pady=(0, 5)
)

red_led_circle = led_canvas.create_oval(
    35,
    5,
    65,
    35,
    fill="#A0A0A0",
    outline="#606060",
    width=2
)

blue_led_circle = led_canvas.create_oval(
    145,
    5,
    175,
    35,
    fill="#A0A0A0",
    outline="#606060",
    width=2
)

led_canvas.create_text(
    50,
    50,
    text="High",
    font=("Arial", 9, "bold"),
    fill="#8B0000"
)

led_canvas.create_text(
    160,
    50,
    text="Low",
    font=("Arial", 9, "bold"),
    fill="#003F7F"
)


# ============================================================
# Button Container
# ============================================================
button_container = tk.Frame(
    root,
    bg="#E8E8E8"
)

button_container.pack(
    pady=(2, 8)
)


# ============================================================
# Heat Button
# ============================================================
heat_frame = tk.Frame(
    button_container,
    bg="#E8E8E8"
)

heat_frame.grid(
    row=0,
    column=0,
    padx=8
)

heat_label = tk.Label(
    heat_frame,
    text="Heat Thermistor",
    font=("Arial", 10),
    bg="#E8E8E8",
    fg="#202020"
)

heat_label.pack(
    anchor="w"
)

heat_button = tk.Button(
    heat_frame,
    text="Heat Thermistor",
    width=15,
    height=1,
    font=("Arial", 10),
    fg="#D00000",
    bg="#F0F0F0",
    activeforeground="#D00000",
    activebackground="#FFCCCC",
    relief="raised",
    bd=2,
    cursor="hand2"
)

heat_button.pack()

heat_button.bind(
    "<ButtonPress-1>",
    heat_press
)

heat_button.bind(
    "<ButtonRelease-1>",
    heat_release
)

heat_button.bind(
    "<Leave>",
    stop_heating_if_mouse_leaves
)


# ============================================================
# Cool Button
# ============================================================
cool_frame = tk.Frame(
    button_container,
    bg="#E8E8E8"
)

cool_frame.grid(
    row=0,
    column=1,
    padx=8
)

cool_label = tk.Label(
    cool_frame,
    text="Cool Thermistor",
    font=("Arial", 10),
    bg="#E8E8E8",
    fg="#202020"
)

cool_label.pack(
    anchor="w"
)

cool_button = tk.Button(
    cool_frame,
    text="Cool Thermistor",
    width=15,
    height=1,
    font=("Arial", 10),
    fg="#0057D9",
    bg="#F0F0F0",
    activeforeground="#0057D9",
    activebackground="#CCE5FF",
    relief="raised",
    bd=2,
    cursor="hand2"
)

cool_button.pack()

cool_button.bind(
    "<ButtonPress-1>",
    cool_press
)

cool_button.bind(
    "<ButtonRelease-1>",
    cool_release
)

cool_button.bind(
    "<Leave>",
    stop_cooling_if_mouse_leaves
)


# ============================================================
# Initial Terminal Output
# ============================================================
print("\nRunning simulated thermistor task.")
print("Close the UI window to stop.")

print(
    f"Blue LED turns ON below {LOW_TEMP_F:.2f} °F."
)

print(
    f"Red LED turns ON above {HIGH_TEMP_F:.2f} °F."
)

print(
    f"Simulated room temperature is "
    f"{ROOM_TEMP_F:.2f} °F.\n"
)


# ============================================================
# Start Simulation
# ============================================================
start_time = time.perf_counter()
last_serial_print_time = start_time

update_front_panel()
update_simulation()

root.mainloop()


# ============================================================
# Post-Process Plotting
# ============================================================
if elapsed_times:
    plt.figure(
        figsize=(10, 6)
    )

    plt.plot(
        elapsed_times,
        temperatures_f,
        label="Temperature (°F)",
        color="black",
        linewidth=1.5
    )

    plt.axhline(
        y=HIGH_TEMP_F,
        color="red",
        linestyle="--",
        label=(
            f"High threshold "
            f"({HIGH_TEMP_F:.1f} °F)"
        )
    )

    plt.axhline(
        y=LOW_TEMP_F,
        color="blue",
        linestyle="--",
        label=(
            f"Low threshold "
            f"({LOW_TEMP_F:.1f} °F)"
        )
    )

    plt.axhline(
        y=ROOM_TEMP_F,
        color="green",
        linestyle=":",
        label=(
            f"Room temperature "
            f"({ROOM_TEMP_F:.1f} °F)"
        )
    )

    plt.xlabel(
        "Time (seconds)"
    )

    plt.ylabel(
        "Temperature (°F)"
    )

    plt.title(
        "Post-Process Simulated Temperature Data"
    )

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

else:
    print(
        "No simulated temperature data was collected, "
        "so no plot was created."
    )