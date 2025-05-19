import streamlit as st

# Streamlit Header
st.header("🌍 Geopy Nominatim Geocoder")
st.divider()

# Introduction
st.markdown(
    """
    The **Geopy Nominatim Geocoder** is a powerful tool for converting addresses into coordinates and vice versa. 
    It provides robust options for accessing detailed location data through OpenStreetMap.

    Below are some examples and explanations of how to use Nominatim effectively.
    """
)
st.divider()

# Geocode Example
st.subheader("1️⃣ Geocoding an Address")
code_example_geocode = """from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="example_app")
location = geolocator.geocode("175 5th Avenue NYC")

print(location.address)
print((location.latitude, location.longitude))
print(location.raw)"""
st.code(code_example_geocode, language="python")
st.markdown(
    """
    **Output Example:**
    ```
    Address: Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, USA
    Coordinates: (40.7410861, -73.9896297241625)
    Raw Data: {'place_id': '9167009604', 'type': 'attraction', ...}
    ```
    """
)
st.divider()

# Reverse Geocode Example
st.subheader("2️⃣ Reverse Geocoding")
code_example_reverse = """from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="example_app")
location = geolocator.reverse("52.509669, 13.376294")

print(location.address)
print((location.latitude, location.longitude))
print(location.raw)"""
st.code(code_example_reverse, language="python")
st.markdown(
    """
    **Output Example:**
    ```
    Address: Potsdamer Platz, Mitte, Berlin, 10117, Deutschland, European Union
    Coordinates: (52.5094982, 13.3765983)
    Raw Data: {'place_id': '654513', 'osm_type': 'node', ...}
    ```
    """
)
st.divider()

# Address Components
st.subheader("3️⃣ Address Components with `addressdetails=True`")
code_example_address_details = """from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="example_app")
location = geolocator.geocode("Eiffel Tower, Paris", addressdetails=True)

if location:
    address = location.raw.get("address", {})
    for component, value in address.items():
        print(f"{component}: {value}")"""
st.code(code_example_address_details, language="python")
st.markdown(
    """
    **Possible Address Components:**
    - **Continent and Country-Level:**
        - `continent`
        - `country`, `country_code`
    - **Administrative Divisions:**
        - `region`, `state`, `state_district`
        - `county`, `municipality`
        - `ISO3166-2-lvl`
    - **Locality:**
        - `city`, `town`, `village`
        - `hamlet`, `croft`, `isolated_dwelling`
    - **Sub-Locality:**
        - `city_district`, `district`, `borough`
        - `suburb`, `subdivision`, `neighbourhood`
        - `allotments`, `quarter`
    - **Detailed Areas:**
        - `city_block`, `residential`, `farm`, `farmyard`
        - `industrial`, `commercial`, `retail`
    - **Specific Address Details:**
        - `road`, `house_number`, `house_name`
    - **Points of Interest:**
        - `tourism`, `natural`, `historic`
        - `military`, `emergency`
    - **Other Attributes:**
        - `postcode`
        - `landuse`, `place`, `boundary`
        - `amenity`, `aeroway`, `waterway`, `railway`
        - `man_made`, `shop`, `leisure`, `office`
        - `club`, `craft`, `bridge`, `tunnel`, `mountain_pass`

    **Sample Output:**
    ```
    continent: Europe
    country: France
    country_code: fr
    state: Île-de-France
    county: Paris
    city: Paris
    postcode: 75007
    road: Champ de Mars
    tourism: Eiffel Tower
    ```
    """
)
st.divider()

# Usage Tips
st.subheader("💡 Tips for Using Nominatim")
st.markdown(
    """
    - Always specify a **`user_agent`** to identify your application.
    - Use **`exactly_one=False`** to get multiple results for ambiguous queries.
    - Handle exceptions for cases where the geocoding service is unavailable.
    - Use **`timeout`** to avoid indefinite waits for a response.

    **Example:**
    ```python
    location = geolocator.geocode("Eiffel Tower", timeout=10, exactly_one=False)
    ```
    """
)
