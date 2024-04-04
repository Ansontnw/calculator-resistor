import streamlit as st

st.title("Hello, Wellcome to my Resistor Calculator👋")
st.write("This is an app that can help us calculate the resistance value")

st.header("Connection Type")
connectionType = st.radio("Please select the type of conncetion", ("Series", "Parallel"))
if connectionType:
    st.write("You selected {} connection.".format(connectionType))

if connectionType == "Series":
     n = st.number_input("Enter the number of resistors in series:", min_value = 1, step = 1, value = 1)
     resistors = []
     for i in range(n):
            r = st.number_input(f"Enter resistance {i + 1} (in ohms):")
            resistors.append(r)
     total_resistance = sum(resistors)
     st.write("Totol value resistance in series is {:.2f} ohms.".format(total_resistance))

elif connectionType == "Parallel":
     n = st.number_input("Enter the number of resistors in parallel:", min_value=1, step=1, value=1)
     resistors = []
     for i in range(n):
          r = st.number_input(f"Enter resistance {i + 1} (in ohms):")
          resistors.append(r)

     # Check if any resistor value is zero
     if 0 in resistors:
         st.write("One or more resistor values is zero. Cannot calculate parallel resistance.")
     else:
         total_resistance = 1 / sum(1 / r for r in resistors)
         st.write("Total resistance value in parallel is {:.2f} ohms.".format(total_resistance))

#elif connectionType == "Parallel":
 #    n = st.number_input("Enter the number of resistors in parallel:", min_value = 1, step = 1, value = 1)
  #   resistors = []
   #  for i in range(n):
    #      r = st.number_input(f"Enter resistance {i + 1} (in ohms):")
     #     resistors.append(r)
     #total_resistance = 1 / sum(float(1 / r for r in resistors))
     #st.write("Total value resistance in series is {:.2f} ohms.".format(total_resistance))
