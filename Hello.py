import streamlit as st

st.title("Hello, Welcome to Resistor Calculator👋")
st.write("*This Project Is Create By Group 4*")
st.write("*Our Group Members is ANSON, AZNUL, AZHAD and FIDAUS*")
st.write("This is an app that can help us calculate the resistance value")

st.header("Connection Type")
connectionType = st.radio("Please select the type of conncetion", ("Series", "Parallel"))
if connectionType:
    st.write("You selected {} connection.".format(connectionType))

st.header("Calculating Resistance")
if connectionType == "Series":
     numRes = st.slider("Enter the number of resistors in series:", min_value = 1, step = 1, value = 1, max_value = 50)
     resistors = []
     for i in range(numRes):
            valRes = st.number_input(f"Enter resistance {i + 1} (in ohms):")
            resistors.append(valRes)
     total_resistance = sum(resistors)
     st.header("Totol values resistance in series is {:.2f} ohms.".format(total_resistance))

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
         st.header("Total value resistance in parallel is {:.2f} ohms.".format(total_resistance))

#elif connectionType == "Parallel":
#     n = st.number_input("Enter the number of resistors in parallel:", min_value = 1, step = 1, value = 1)
#     resistors = []
#     for i in range(n):
#          r = st.number_input(f"Enter resistance {i + 1} (in ohms):")
#          resistors.append(r)
#     total_resistance = 1 / sum(float(1 / r for r in resistors))
#     st.write("Total value resistance in series is {:.2f} ohms.".format(total_resistance))
