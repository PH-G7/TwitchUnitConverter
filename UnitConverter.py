from TwitchWebsocket import TwitchWebsocket # type: ignore
import json, requests, random, logging # type: ignore

from enum import Enum, auto
from Log import Log # type: ignore
Log(__file__)

from Settings import Settings # type: ignore

class ResultCode(Enum):
    SUCCESS = auto()
    ERROR = auto()

class UnitConverter:
    def __init__(self):
        # Initialize variables
        self.host = None
        self.port = None
        self.chan = None
        self.nick = None
        self.auth = None

        # Fill uninitialized variables using settings.txt
        self.update_settings()

        # Instantiate TwitchWebsocket instance with correct params
        self.ws = TwitchWebsocket(host=self.host, 
                                  port=self.port,
                                  chan=self.chan,
                                  nick=self.nick,
                                  auth=self.auth,
                                  callback=self.message_handler,
                                  capability=None,
                                  live=True)
        
        # Start the websocket connection
        self.ws.start_bot()
        
    def update_settings(self):
        # Fill previously initialised variables with data from the settings.txt file
        self.host, self.port, self.chan, self.nick, self.auth = Settings().get_settings()

    def message_handler(self, m):
        try:
            if m.type == "366":
                logging.info(f"Successfully joined channel: #{m.channel}")
            
            elif m.type == "PRIVMSG":
                # Listen for command
                if m.message.startswith("!ctof"):
                    # Extract temperature from message
                    temperature = m.message.split(" ")[1]
                    temperature = float(temperature)

                    # Convert Celsius to Fahrenheit
                    out, _code = self.convert(temperature, "Celsius")
                    # Send message to twitch chat
                    self.ws.send_message(out)

                elif m.message.startswith("!ftoc"):
                    # Extract temperature from message
                    temperature = m.message.split(" ")[1]
                    temperature = float(temperature)

                    # Convert Fahrenheit to Celsius
                    out, _code = self.convert(temperature, "Fahrenheit")
                    # Send message to twitch chat
                    self.ws.send_message(out)

                elif m.message.startswith("!mtoft"):
                    # Extract meters from message
                    meters = m.message.split(" ")[1]
                    meters = float(meters)

                    # Convert meters to feet
                    out, _code = self.convert(meters, "Meters")
                    # Send message to twitch chat
                    self.ws.send_message(out)

                elif m.message.startswith("!fttom"):
                    # Extract feet from message
                    feet = m.message.split(" ")[1]
                    feet = float(feet)

                    # Convert feet to meters
                    out, _code = self.convert(feet, "Feet")
                    # Send message to twitch chat
                    self.ws.send_message(out)

                elif m.message.startswith("!kmtomi"):
                    # Extract kilometers from message
                    kilometers = m.message.split(" ")[1]
                    kilometers = float(kilometers)

                    # Convert kilometers to miles
                    out, _code = self.convert(kilometers, "Kilometers")
                    # Send message to twitch chat
                    self.ws.send_message(out)

                elif m.message.startswith("!mitokm"):
                    # Extract miles from message
                    miles = m.message.split(" ")[1]
                    miles = float(miles)

                    # Convert miles to kilometers
                    out, _code = self.convert(miles, "Miles")
                    # Send message to twitch chat
                    self.ws.send_message(out)   

                elif m.message.startswith("!cmtoin"):
                    # Extract centimeters from message
                    centimeters = m.message.split(" ")[1]
                    centimeters = float(centimeters)

                    # Convert centimeters to inches
                    out, _code = self.convert(centimeters, "Centimeters")
                    # Send message to twitch chat
                    self.ws.send_message(out)

                elif m.message.startswith("!intocm"):
                    # Extract inches from message
                    inches = m.message.split(" ")[1]
                    inches = float(inches)

                    # Convert inches to centimeters
                    out, _code = self.convert(inches, "Inches")
                    # Send message to twitch chat
                    self.ws.send_message(out)

                elif m.message.startswith("!kgtolbs"):
                    # Extract kilograms from message
                    kilograms = m.message.split(" ")[1]
                    kilograms = float(kilograms)

                    # Convert kilograms to pounds
                    out, _code = self.convert(kilograms, "Kilograms")
                    # Send message to twitch chat
                    self.ws.send_message(out)

                elif m.message.startswith("!lbstokg"):
                    # Extract pounds from message
                    pounds = m.message.split(" ")[1]
                    pounds = float(pounds)

                    # Convert pounds to kilograms
                    out, _code = self.convert(pounds, "Pounds")
                    # Send message to twitch chat
                    self.ws.send_message(out)
                
                elif m.message.startswith("!oztog"):
                    # Extract ounces from message
                    ounces = m.message.split(" ")[1]
                    ounces = float(ounces)

                    # Convert ounces to grams
                    out, _code = self.convert(ounces, "Ounces")
                    # Send message to twitch chat
                    self.ws.send_message(out)

                elif m.message.startswith("!gtooz"):
                    # Extract grams from message
                    grams = m.message.split(" ")[1]
                    grams = float(grams)

                    # Convert grams to ounces
                    out, _code = self.convert(grams, "Grams")
                    # Send message to twitch chat
                    self.ws.send_message(out)

                elif m.message.startswith("!floztoml"):
                    # Extract fluid ounces from message
                    fluid_ounces = m.message.split(" ")[1]
                    fluid_ounces = float(fluid_ounces)

                    # Convert fluid ounces to milliliters
                    out, _code = self.convert(fluid_ounces, "Fluid Ounces")
                    # Send message to twitch chat
                    self.ws.send_message(out)

                elif m.message.startswith("!mltofloz"):
                    # Extract milliliters from message
                    milliliters = m.message.split(" ")[1]
                    milliliters = float(milliliters)

                    # Convert milliliters to fluid ounces
                    out, _code = self.convert(milliliters, "Milliliters")
                    # Send message to twitch chat
                    self.ws.send_message(out)

                elif m.message.startswith("!galtol"):
                    # Extract gallons from message
                    gallons = m.message.split(" ")[1]
                    gallons = float(gallons)

                    # Convert gallons to liters
                    out, _code = self.convert(gallons, "Gallons")
                    # Send message to twitch chat
                    self.ws.send_message(out)

                elif m.message.startswith("!ltogal"):
                    # Extract liters from message
                    liters = m.message.split(" ")[1]
                    liters = float(liters)

                    # Convert liters to gallons
                    out, _code = self.convert(liters, "Liters")
                    # Send message to twitch chat
                    self.ws.send_message(out)                            
        
        except Exception as e:
            logging.exception(e)

    def convert(self, value, from_unit):
        # Perform the conversion
        if from_unit == "Celsius":
                converted_temperature = (value * 9/5) + 32
                out = f"{value}°C is {converted_temperature:.1f}°F"
        elif from_unit == "Fahrenheit":
                converted_temperature = (value - 32) * 5/9
                out = f"{value}°F is {converted_temperature:.1f}°C"
        elif from_unit == "Meters":
                converted_distance = value * 3.28084
                out = f"{value}m is {converted_distance:.2f}ft"
        elif from_unit == "Feet":
                converted_distance = value / 3.28084
                out = f"{value}ft is {converted_distance:.2f}m"
        elif from_unit == "Kilometers":
                converted_distance = value * 0.621371
                out = f"{value}km is {converted_distance:.1f}mi"
        elif from_unit == "Miles":
                converted_distance = value / 0.621371
                out = f"{value}mi is {converted_distance:.1f}km"
        elif from_unit == "Centimeters":
                converted_distance = value / 2.54
                out = f"{value}cm is {converted_distance:.2f}in"
        elif from_unit == "Inches":
                converted_distance = value * 2.54
                out = f"{value}in is {converted_distance:.2f}cm"
        elif from_unit == "Kilograms":
                converted_weight = value * 2.20462
                out = f"{value}kg is {converted_weight:.1f}lbs"
        elif from_unit == "Pounds":
                converted_weight = value / 2.20462
                out = f"{value}lbs is {converted_weight:.1f}kg"
        elif from_unit == "Ounces":
                converted_weight = value * 28.3495
                out = f"{value}oz is {converted_weight:.0f}g"
        elif from_unit == "Grams":
                converted_weight = value / 28.3495
                out = f"{value}g is {converted_weight:.2f}oz"
        elif from_unit == "Fluid Ounces":
                converted_volume = value * 29.5735
                out = f"{value}fl oz is {converted_volume:.0f}mL"
        elif from_unit == "Milliliters":
                converted_volume = value / 29.5735
                out = f"{value}mL is {converted_volume:.2f}fl oz"
        elif from_unit == "Gallons":
                converted_volume = value * 3.78541
                out = f"{value}gal is {converted_volume:.2f}L"
        elif from_unit == "Liters":
                converted_volume = value / 3.78541
                out = f"{value}L is {converted_volume:.2f}gal"

        return out, ResultCode.SUCCESS
    
if __name__ == "__main__":
    UnitConverter()
