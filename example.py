import openjub_py

token = "<token here>" # Set your token here.

# Create a new client
client = openjub_py.Client(token)

# Show information about a particular user account
client.user_account("dkundel")
