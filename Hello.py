import streamlit as st

st.title("Hello, Welcome to Resistor Calculator👋")

st.write("*This Project Is Create By Group 4*")
st.write("*Our Group Members is ANSON, AZNUL, AZHAD and FIDAUS*")
st.write("This is an app that can help us calculate the resistor and resistance value")

st.title("Resistance Calculator")
st.header("Connection Type")

connectionType = st.radio("Please select the type of conncetion", ("Series", "Parallel"))
if connectionType:
    st.write("You selected {} connection.".format(connectionType))

st.header("Calculating Resistance")

if connectionType == "Series":
     numRes = st.number_input("Enter the number of resistors in series:", min_value = 1, step = 1, value = 1)
     resistors = []
     for i in range(numRes):
            valRes = st.number_input(f"Enter resistance {i + 1} (in ohms):")
            resistors.append(valRes)
     total_resistance = sum(resistors)
     st.subheader("Totol values resistance in series is {:.2f} Ω.".format(total_resistance))

elif connectionType == "Parallel":
     numRes = st.number_input("Enter the number of resistors in parallel:", min_value=1, step=1, value=1)
     resistors = []
     for i in range(numRes):
          valRes = st.number_input(f"Enter resistance {i + 1} (in ohms):")
          resistors.append(valRes)
     if 0 in resistors:
         st.write("If resistor values is zero. Cannot calculate parallel resistance.")
     else:
         total_resistance = 1 / sum(1 / valRes for valRes in resistors)
         st.subheader("Total value resistance in parallel is {:.2f} Ω.".format(total_resistance))

st.title("Resistor Calculator")

ColorBand1 = st.radio("Pick the first band color resistor", ("Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Grey", "White"))
ColorBand2 = st.radio("Pick the second band color resistor", ("Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Grey", "White"))
ColorBand3 = st.radio("Pick the third band color resistor", ("Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Grey", "White"))
ColorBand4 = st.radio("Pick the fourth band color resistor", ("Gold", "Silver", "No color"))

color_values = {
    "Black": 0,
    "Brown": 1,
    "Red": 2,
    "Orange": 3,
    "Yellow": 4,
    "Green": 5,
    "Blue": 6,
    "Purple": 7,
    "Grey": 8,
    "White": 9
}

multiplier_values = {
    "Black": 1,
    "Brown": 10,
    "Red": 100,
    "Orange": 1000,
    "Yellow": 10000,
    "Green": 100000,
    "Blue": 1000000,
    "Purple": 10000000,
    "Grey": 100000000,
    "White": 1000000000
}

tolerance_values = {
    "Gold": "±5%",
    "Silver": "±10%",
    "No color": "±20%"
}

Val1 = color_values[ColorBand1]
Val2 = color_values[ColorBand2]
Val3 = multiplier_values[ColorBand3]
Val4 = tolerance_values[ColorBand4]

ResVal = (Val1 * 10 + Val2) * Val3

st.write(f"<h1>Resistance Value: {ResVal} ohms, Tolerance: {Val4}</h1>", unsafe_allow_html=True)

#elif connectionType == "Parallel":
#     n = st.number_input("Enter the number of resistors in parallel:", min_value = 1, step = 1, value = 1)
#     resistors = []
#     for i in range(n):
#          r = st.number_input(f"Enter resistance {i + 1} (in ohms):")
#          resistors.append(r)
#     total_resistance = 1 / sum(float(1 / r for r in resistors))
#     st.write("Total value resistance in series is {:.2f} ohms.".format(total_resistance))
