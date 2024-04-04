# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
     n = st.number_input("Enter the number of resistors in parallel:", mi_value = 1, step = 1, value = 1)
     resistors = []
     for i in range(n):
          r = st.number_input(f"Enter resistance {i + 1} (in ohms):")
          resistors.append(r)
     total_resistance = 1 / sum(1 / r for r in resistors)
     st.write("Totol value resistance in series is {:.2f} ohms.".format(total_resistance))
