Level 1: Foundations of Test & Engineering Thinking
===================================================

.. image:: _static/media/image1.png
   :alt: Level 1 student manual cover
   :align: center
   :width: 80%

.. contents:: On This Page
   :local:
   :depth: 2


About This Workshop
-------------------

Level 1 introduces the foundations of test engineering through a
greenhouse temperature-monitoring challenge.

This online version of the workshop uses a software simulation. Instead
of connecting a physical thermistor and LEDs to measurement hardware,
you will interact with a simulated thermistor, collect simulated
temperature data, analyze the results, and observe how the system
responds.

The simulation follows the same engineering workflow used during the
in-person workshop:

**Physical Phenomenon → Sensor → Acquisition → Analysis → Decision → Action**

.. note::

   During the in-person workshop, students use a real thermistor,
   warning LEDs, a breadboard, and an NI mioDAQ.

   In this supplemental version, Python or LabVIEW generates the
   temperature measurements and simulates the warning indicators.

   The source of the data is different, but the engineering process is
   the same.


Test in Engineering
-------------------

Every day, we interact with products that we rarely think twice about.

- You expect your phone to connect to Wi-Fi.
- You expect your car to start.
- You expect your headphones to connect to Bluetooth.
- You expect the elevator to stop at the correct floor.
- You expect your GPS to tell you where you are.

But how do we know these systems will work?

The answer is testing.


What Is Test?
^^^^^^^^^^^^^

Test in engineering is the process of evaluating the performance,
reliability, safety, and quality of a product before it reaches the
customer.

Engineers design experiments, collect data, and build automated systems
that help answer one of the most important questions in engineering:

**How do we know this works?**

Rather than relying on assumptions, engineers use measurements and data
to verify that a product behaves as expected.

Testing provides the evidence needed to answer questions such as:

- Does the product work?
- How well does it work?
- What happens if it fails?
- Does it meet its requirements?
- How can it be improved?


Hardware and Software Test
^^^^^^^^^^^^^^^^^^^^^^^^^^

Testing exists in many forms, but it often looks different depending on
what is being tested.

+------------------------------------+------------------------------------+
| Hardware Testing                   | Software Testing                   |
+====================================+====================================+
| Tests physical products            | Tests software and applications    |
+------------------------------------+------------------------------------+
| Uses sensors, instruments, code,   | Uses code and test scripts         |
| and test systems                   |                                    |
+------------------------------------+------------------------------------+
| Focuses on physical performance,   | Focuses on functionality and user  |
| quality, and reliability           | experience                         |
+------------------------------------+------------------------------------+
| Example: Medical device            | Example: Mobile application        |
+------------------------------------+------------------------------------+

This workshop focuses on the principles of hardware testing. However,
the online activity uses software to simulate the behavior of a physical
measurement system.


The Product Life Cycle
----------------------

What Is It?
^^^^^^^^^^^

The Product Life Cycle is the journey a product takes from an initial
idea to something customers use in the real world.

For engineers, the lifecycle commonly includes:

- Research
- Design
- Prototyping
- Verification and validation
- Production
- Deployment
- Continued improvement

.. figure:: _static/media/image2.png
   :width: 80%
   :align: center
   :alt: Product Development Life Cycle diagram

   Figure 1. Product Development Life Cycle.

Testing does not happen only after a product is finished. Engineers test
ideas during research, verify design assumptions, evaluate prototypes,
inspect products during manufacturing, and monitor performance after
deployment.

Two especially important phases are:

- **Verification and Validation**, or V&V
- **Production**

**Verification and Validation asks:**

   Did we design the product correctly?

**Production testing asks:**

   Did we build the product correctly?


Verification and Validation Testing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before a company manufactures thousands or millions of products,
engineers need confidence that the design will perform as expected.

V&V testing is performed on prototypes and early product designs to
evaluate functionality, performance, reliability, safety, and other
requirements.

+-------------------+--------------------------------------------------+
| Type of Test      | Questions It Answers                             |
+===================+==================================================+
| Functional        | Does the product do what it was designed to do?  |
+-------------------+--------------------------------------------------+
| Performance       | How well does the product perform?               |
+-------------------+--------------------------------------------------+
| Reliability       | Will it continue working over time?              |
+-------------------+--------------------------------------------------+
| Environmental     | Can it survive where it will be used?            |
+-------------------+--------------------------------------------------+
| Stress            | What happens outside normal conditions?          |
+-------------------+--------------------------------------------------+
| Safety            | Does the product operate safely?                 |
+-------------------+--------------------------------------------------+


Production Testing
^^^^^^^^^^^^^^^^^^

Once engineers have confidence in the design, the next challenge is
manufacturing products consistently.

Production testing occurs during manufacturing and helps ensure that
each unit meets its quality and performance requirements.

Unlike V&V, which focuses on learning about and proving the design,
production testing focuses on:

- Speed
- Repeatability
- Quality
- Consistency
- Pass/fail decisions


V&V Versus Production
^^^^^^^^^^^^^^^^^^^^^

+--------------------------------+--------------------------------------+
| Verification and Validation    | Production                           |
+================================+======================================+
| Proves the design works        | Proves each manufactured unit works  |
+--------------------------------+--------------------------------------+
| Focuses on prototypes          | Focuses on finished products         |
+--------------------------------+--------------------------------------+
| Finds design issues            | Finds manufacturing issues           |
+--------------------------------+--------------------------------------+
| Emphasizes learning            | Emphasizes quality and consistency    |
+--------------------------------+--------------------------------------+
| “Did we design it correctly?”  | “Did we build it correctly?”         |
+--------------------------------+--------------------------------------+


Why Testing Matters
-------------------

When someone buys a product, they trust that it will perform as
expected.

Testing helps engineers build that trust by identifying problems before
customers encounter them. Without testing, companies risk safety
failures, recalls, expensive redesigns, and inconsistent products.

At its core, testing reduces uncertainty.

It transforms:

**We think it works.**

into:

**We have evidence that it works.**

Good testing requires engineers to:

- Ask clear questions
- Define requirements
- Collect reliable measurements
- Analyze data
- Compare results against expectations
- Make evidence-based decisions


The Measurement Chain
---------------------

Engineering decisions begin with information from the physical world.

The process of turning a real-world condition into useful information is
called the **measurement chain**.

.. image:: _static/media/image5.png
   :alt: Measurement chain
   :align: center
   :width: 90%

The measurement chain used in this workshop is:

**Physical Phenomenon → Sensor → Acquisition → Analysis → Decision → Action**

In the in-person workshop, a thermistor and mioDAQ create and acquire a
physical electrical signal.

In this supplemental workshop, software simulates the temperature and
sensor response. The measurements are simulated, but the analysis,
decision logic, indicators, and engineering thought process remain the
same.


Simulated Greenhouse Challenge
------------------------------

Project Scenario
^^^^^^^^^^^^^^^^

Imagine you work for a climate-control company that supports commercial
greenhouses.

Your customer needs a temperature-monitoring system that helps protect
crops from extreme temperatures.

Your job is to evaluate a simulated system that monitors temperature
and warns operators when conditions move outside an acceptable range.

The system must:

- Continuously monitor greenhouse temperature.
- Maintain a target range of 70°F to 85°F.
- Turn on a blue indicator below 70°F.
- Turn on a red indicator above 85°F.
- Display the current system status.
- Provide a clear warning when conditions are unsafe.


In-Person and Simulation Experiences
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Both versions follow the same measurement chain, but they generate and
acquire data differently.

+----------------------+--------------------------------+--------------------------------+
| Step                 | In-Person Workshop             | Simulation Workshop            |
+======================+================================+================================+
| Physical phenomenon  | Real temperature               | Simulated temperature          |
+----------------------+--------------------------------+--------------------------------+
| Sensor               | Physical thermistor            | Simulated thermistor response  |
+----------------------+--------------------------------+--------------------------------+
| Signal               | Electrical voltage             | Software-generated value       |
+----------------------+--------------------------------+--------------------------------+
| Acquisition          | NI mioDAQ                       | Python or LabVIEW loop         |
+----------------------+--------------------------------+--------------------------------+
| Analysis             | Convert and compare data       | Compare simulated temperature  |
+----------------------+--------------------------------+--------------------------------+
| Decision             | Hot, cold, or acceptable       | Hot, cold, or acceptable       |
+----------------------+--------------------------------+--------------------------------+
| Action               | Physical warning LEDs          | Simulated LED indicators       |
+----------------------+--------------------------------+--------------------------------+

.. important::

   A simulation helps us study the logic and behavior of a measurement
   system, but it does not replace every aspect of working with real
   hardware.

   Real measurements can be affected by sensor accuracy, electrical
   noise, wiring, signal conditioning, input range, grounding, and the
   physical environment.


Physical Phenomenon
^^^^^^^^^^^^^^^^^^^

A physical phenomenon is something happening in the real world that we
want to observe or measure.

Examples include temperature, pressure, force, motion, light, and sound.

For this project, the physical phenomenon is greenhouse temperature.

In the in-person workshop, the temperature surrounding a physical
thermistor changes. In the simulation, software creates a changing
temperature value that represents greenhouse conditions.

**Think About It**

- What could happen if a greenhouse becomes too hot?
- What could happen if it becomes too cold?
- Why would operators need a warning system?


Sensor
^^^^^^

A sensor detects a physical phenomenon and converts it into a signal
that a measurement system can use.

The in-person workshop uses a real thermistor. A thermistor changes
resistance as its temperature changes.

The simulation represents the thermistor in software.

Pressing **Heat Thermistor** or **Cool Thermistor** changes the
simulated temperature that would normally be influenced by the physical
sensor and its environment.


Signal Conditioning
^^^^^^^^^^^^^^^^^^^

Signal conditioning prepares a sensor signal so it can be measured
accurately and safely.

A physical thermistor does not directly produce a temperature value that
a computer can understand. It changes resistance. A circuit and
measurement device convert that changing resistance into a measurable
voltage.

Signal conditioning can help:

- Reduce noise
- Amplify small signals
- Provide sensor excitation
- Protect measurement equipment
- Match the signal to the DAQ input
- Address nonlinear sensor behavior
- Improve measurement quality

In the simulation, we do not physically condition an electrical signal.
The program directly generates a simulated temperature.

This allows us to focus on the rest of the measurement chain, but it is
important to remember that a real measurement system must account for
the sensor's electrical behavior.


Acquisition
^^^^^^^^^^^

Acquisition is the step where a system collects measurements and makes
the data available to the computer.

During the in-person workshop, the mioDAQ acquires voltage from the
thermistor circuit.

During the simulation, a timed software loop generates and records a new
temperature value every 100 milliseconds.

The simulation begins at a room temperature of 70°F.

- Holding **Heat Thermistor** increases the simulated temperature.
- Holding **Cool Thermistor** decreases the simulated temperature.
- Releasing both buttons allows the temperature to move toward 70°F.

Although the source is different, the program still collects a sequence
of measurements over time.


Analysis
^^^^^^^^

Analysis is the step where data becomes useful information.

The simulation compares the current temperature against the greenhouse
requirements:

- Below 70°F means the greenhouse is too cold.
- From 70°F through 85°F means the greenhouse is in the ideal range.
- Above 85°F means the greenhouse is overheating.

The simulation also records the temperature and elapsed time.

When the simulation ends, Python displays a graph of temperature versus
time so you can examine how the greenhouse changed during the test.


Decision and Action
^^^^^^^^^^^^^^^^^^^

The simulated system uses the following logic:

+-------------------------+----------------+---------------------------+
| Condition               | System Status  | Action                    |
+=========================+================+===========================+
| Temperature below 70°F  | TOO COLD       | Blue indicator turns on   |
+-------------------------+----------------+---------------------------+
| Temperature from        | IDEAL          | Both indicators remain    |
| 70°F through 85°F       |                | off                       |
+-------------------------+----------------+---------------------------+
| Temperature above 85°F  | OVERHEATING    | Red indicator turns on    |
+-------------------------+----------------+---------------------------+

In a real greenhouse, the final action could activate a fan, heater,
alarm, or ventilation system.

In this simulation, the red and blue indicators communicate the
decision without controlling physical equipment.


Python Simulation
-----------------

What You Need
^^^^^^^^^^^^^

To complete the Python simulation, install:

- Python 3
- Visual Studio Code
- The Microsoft Python extension for Visual Studio Code
- Matplotlib


Install Python
^^^^^^^^^^^^^^

1. Visit the `official Python download page
   <https://www.python.org/downloads/>`_.

2. Download Python 3 for your operating system.

3. Run the installer.

4. If the installer provides an option to add Python to your system
   path, select it.

5. Complete the installation.

On Windows, open a terminal and verify the installation:

.. code-block:: console

   py --version

If that command is not recognized, try:

.. code-block:: console

   python --version


Install Visual Studio Code
^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Visit the `Visual Studio Code download page
   <https://code.visualstudio.com/download>`_.

2. Download the installer for your operating system.

3. Run the installer.

4. Open Visual Studio Code.

.. note::

   Visual Studio and Visual Studio Code are different applications.

   This workshop uses **Visual Studio Code**.


Install the Python Extension
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Open Visual Studio Code.

2. Select the **Extensions** icon on the left side of the window.

3. Search for ``Python``.

4. Select the Python extension published by Microsoft.

5. Select **Install**.


Select the Python Interpreter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Press ``Ctrl+Shift+P`` in Visual Studio Code.

2. Enter:

.. code-block:: text

   Python: Select Interpreter

3. Select the Python installation you installed earlier.


Install Matplotlib
^^^^^^^^^^^^^^^^^^

In Visual Studio Code, select:

**Terminal → New Terminal**

Enter:

.. code-block:: console

   py -m pip install matplotlib

If your computer does not recognize ``py``, use:

.. code-block:: console

   python -m pip install matplotlib


Download the Python Simulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Select the link below to download the complete Python greenhouse
simulation.

:download:`Download Simulation ThermistorWithLED Python.py
<_static/downloads/Simulation ThermistorWithLED Python.py>`

.. tip::

   Save the file somewhere easy to find, such as your Downloads folder.

   Make sure the filename still ends in ``.py``.


View the Python Code Online
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can review the complete Python program below before downloading it.

.. literalinclude:: _static/downloads/Simulation ThermistorWithLED Python.py
   :language: python
   :linenos:
   :caption: Complete Python Greenhouse Simulation
   :name: python-greenhouse-simulation


Open the Downloaded Python Code
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Open Visual Studio Code.

2. Select **File → Open File**.

3. Select ``Simulation ThermistorWithLED Python.py``.

4. Confirm that a Python interpreter is selected.

5. Select the **Run Python File** button in the upper-right corner.


Enter the Temperature Requirements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A terminal will open at the bottom of Visual Studio Code.

Enter the high-temperature threshold:

.. code-block:: text

   Enter the high temperature threshold in °F: 85

Then enter the low-temperature threshold:

.. code-block:: text

   Enter the low temperature threshold in °F: 70

Press **Enter** after each value.

The simulated front panel will open in a separate window.


Explore the Simulated Front Panel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The simulated front panel includes:

**Temperature**
   Displays the current simulated temperature in Fahrenheit and Celsius.

**Status**
   Displays IDEAL, TOO COLD, or OVERHEATING.

**High indicator**
   Represents the red warning LED in the in-person system.

**Low indicator**
   Represents the blue warning LED in the in-person system.

**Heat Thermistor**
   Increases the simulated temperature while the button is held.

**Cool Thermistor**
   Decreases the simulated temperature while the button is held.


Python Simulation Activity
--------------------------

Test 1: Normal Conditions
^^^^^^^^^^^^^^^^^^^^^^^^^

Allow the simulation to run without pressing either button.

Observe:

- The current temperature
- The system status
- The red indicator
- The blue indicator

**Think About It**

- Is the greenhouse within the acceptable range?
- Are either of the warning indicators on?
- Does the system meet the greenhouse requirement?


Test 2: Overheating
^^^^^^^^^^^^^^^^^^^

Press and hold **Heat Thermistor**.

Continue heating until the temperature rises above the high threshold.

Observe:

- The temperature at which the status changes
- The text displayed in the status window
- The red indicator
- The blue indicator

**Think About It**

- Why does the red indicator remain off at exactly 85°F?
- At what point does the Boolean condition become true?
- What real greenhouse action could replace the red indicator?


Test 3: Recovery
^^^^^^^^^^^^^^^^

Release the **Heat Thermistor** button.

Observe how the simulated temperature moves toward room temperature.

Watch what happens when the temperature returns to the acceptable range.

**Think About It**

- When does the red indicator turn off?
- What causes the status to return to IDEAL?
- Is the system measuring, analyzing, and deciding continuously?


Test 4: Too Cold
^^^^^^^^^^^^^^^^

Press and hold **Cool Thermistor**.

Continue cooling until the temperature falls below the low threshold.

Observe:

- The temperature at which the status changes
- The blue indicator
- The status display
- The terminal output

**Think About It**

- Why does the blue indicator remain off at exactly 70°F?
- What action might a real greenhouse system take?
- How is the decision connected to the greenhouse requirement?


Test 5: Analyze the Data
^^^^^^^^^^^^^^^^^^^^^^^^

Close the simulation window after testing the hot, ideal, and cold
conditions.

The program will display:

- A message showing that the simulation stopped
- The number of simulated readings collected
- A graph of temperature versus time

Use the graph to identify:

1. When heating began
2. When the greenhouse exceeded 85°F
3. When the temperature returned to the ideal range
4. When cooling began
5. When the greenhouse fell below 70°F
6. When both warning indicators were off


Optional LabVIEW Simulation
---------------------------

LabVIEW is a graphical programming environment. Instead of writing only
text-based instructions, LabVIEW programs are created by connecting
functions and structures with wires.

The LabVIEW simulation follows the same greenhouse requirements and
measurement-chain workflow as the Python simulation.


Install LabVIEW Community Edition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Visit the `NI LabVIEW Community Edition download page
   <https://www.ni.com/en/support/downloads/software-products/download.labview-community.html>`_.

2. Sign in with an NI account or create an account.

3. Select LabVIEW Community Edition.

4. Run the installer.

5. Follow the installation prompts.

6. Open LabVIEW after installation.

7. Complete any required sign-in or activation prompts.


Download the LabVIEW Simulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Select the link below to download the LabVIEW greenhouse simulation.

:download:`Download Simulation ThermistorWithLED (1).vi
<_static/downloads/Simulation ThermistorWithLED (1).vi>`

.. note::

   A LabVIEW VI cannot be displayed as text on this page in the same way
   as the Python program.

   Download the VI and open it in LabVIEW to view the Front Panel and
   Block Diagram.


Open the LabVIEW Simulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Open LabVIEW.

2. Select **File → Open**.

3. Select ``Simulation ThermistorWithLED (1).vi``.

4. Open the Front Panel.

5. Select the **Run** arrow.

6. Follow the instructions displayed on the Front Panel.


The LabVIEW Front Panel
^^^^^^^^^^^^^^^^^^^^^^^

The Front Panel is the user interface of a LabVIEW program.

Use the Front Panel to:

- Enter the high and low temperature thresholds
- Heat or cool the simulated thermistor
- View the current temperature
- View the simulated warning indicators
- Stop the simulation

If you have a screenshot of the simulated Front Panel, add it to:

.. code-block:: text

   docs/source/_static/media/labview_simulation_front_panel.png

Then display it here:

.. figure:: _static/media/labview_simulation_front_panel.png
   :width: 85%
   :align: center
   :alt: LabVIEW greenhouse simulation Front Panel

   LabVIEW greenhouse simulation Front Panel.


The LabVIEW Block Diagram
^^^^^^^^^^^^^^^^^^^^^^^^^

The Block Diagram contains the graphical code that controls the
simulation.

Look for the following programming elements:

- While Loop
- Timing function
- Simulated temperature value
- Comparison functions
- Boolean logic
- Case Structure
- Graph or chart
- Stop control

If you have a screenshot of the simulated Block Diagram, add it to:

.. code-block:: text

   docs/source/_static/media/labview_simulation_block_diagram.png

Then display it here:

.. figure:: _static/media/labview_simulation_block_diagram.png
   :width: 95%
   :align: center
   :alt: LabVIEW greenhouse simulation Block Diagram

   LabVIEW greenhouse simulation Block Diagram.


Python and LabVIEW Comparison
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Python and LabVIEW programs look different, but they follow the same
engineering process.

+----------------------+--------------------------------+--------------------------------+
| Engineering Step     | Python                         | LabVIEW                        |
+======================+================================+================================+
| Continuous execution | Tkinter callback loop          | While Loop                     |
+----------------------+--------------------------------+--------------------------------+
| Timing               | Scheduled update interval      | Timing function                |
+----------------------+--------------------------------+--------------------------------+
| Requirements         | Threshold variables            | Numeric controls or constants  |
+----------------------+--------------------------------+--------------------------------+
| Analysis             | Conditional statements         | Comparison functions           |
+----------------------+--------------------------------+--------------------------------+
| Decision             | If/elif/else logic             | Boolean or Case Structure logic|
+----------------------+--------------------------------+--------------------------------+
| Display              | Tkinter interface              | Front Panel indicators         |
+----------------------+--------------------------------+--------------------------------+
| Visualization        | Matplotlib plot                | Waveform chart or graph        |
+----------------------+--------------------------------+--------------------------------+

The programming syntax is different, but the engineering thinking is
the same.


Troubleshooting
---------------

Python Is Not Recognized
^^^^^^^^^^^^^^^^^^^^^^^^

If the terminal does not recognize ``py``, try:

.. code-block:: console

   python --version

If neither command works:

1. Reinstall Python.
2. Confirm that Python is added to your system path.
3. Restart Visual Studio Code.
4. Select the Python interpreter again.


Matplotlib Is Missing
^^^^^^^^^^^^^^^^^^^^^

If the program reports:

.. code-block:: text

   ModuleNotFoundError: No module named 'matplotlib'

Open a Visual Studio Code terminal and run:

.. code-block:: console

   py -m pip install matplotlib

If necessary, use:

.. code-block:: console

   python -m pip install matplotlib


The Program Appears to Be Waiting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check the terminal at the bottom of Visual Studio Code.

The program asks for the high and low temperature thresholds before
opening the simulated front panel.

Enter:

.. code-block:: text

   85

and then:

.. code-block:: text

   70


The LabVIEW VI Will Not Open
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Confirm that:

- LabVIEW is installed.
- The VI download completed.
- The file still has the ``.vi`` extension.
- You are opening the VI from inside LabVIEW.

A VI saved in a newer LabVIEW version may not open in an older LabVIEW
version.


Reflection Questions
--------------------

After completing the simulation, answer the following questions:

1. What physical phenomenon was represented by the simulation?

2. What sensor did the software simulate?

3. How did the program acquire new temperature values?

4. What requirements were used to analyze the data?

5. How did the program determine whether the greenhouse was safe?

6. What actions occurred when the temperature crossed a threshold?

7. How would the experience differ if a real thermistor and mioDAQ were
   used?

8. What measurement challenges can occur with real hardware that are not
   represented by the simulation?

9. What evidence shows that the system behaved as expected?

10. Did the results show that the simulated system met its requirements?


Summary
-------

Throughout this workshop, you followed the same general process that
test engineers use to understand and interact with the world around
them.

You began with a physical phenomenon: greenhouse temperature.

The software represented the response of a temperature sensor, acquired
simulated measurements, analyzed the temperature, compared it against
requirements, made a decision, and updated warning indicators.

Together, these steps form the measurement chain:

**Physical Phenomenon → Sensor → Acquisition → Analysis → Decision → Action**

The simulation does not replace every aspect of real measurement
hardware. It removes physical variables such as wiring, electrical
noise, sensor tolerance, input configuration, and signal conditioning.

However, it allows you to practice the engineering workflow and
understand how measurements become decisions.

Most importantly, you made your first simulated measurement and used
data as evidence.

That is the foundation of test.


Get Certified for Level 1
-------------------------

You have completed the Level 1 online workshop!

To receive credit for completing Level 1, complete the online feedback
survey using the link below.

`Complete the Level 1 Feedback Survey and Certification Form
<https://forms.cloud.microsoft/r/0LK7kuz1Xx>`_

.. important::

   Complete the survey after finishing the Python or LabVIEW simulation.

   Make sure the information you submit is accurate so your Level 1
   workshop completion can be recorded.


Looking Ahead
-------------

In the next level, you will examine what makes a measurement reliable.

You will explore how engineers select sensors and acquisition settings,
interpret sensor specifications, choose sampling configurations, log
data, and determine whether they can trust the results.

Level 1 focused on the question:

**How do we make a measurement?**

Level 2 will begin asking:

**How do we make a good measurement?**
