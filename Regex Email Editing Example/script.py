#!/usr/bin/env python3

# Author: Michael D. Parnell
# Date: June 2024
# Description: This script reads a CSV file containing user email addresses,
#              replaces email addresses with a specified old domain with a new domain,
#              and writes the updated email addresses to a new CSV file.
#-- coding: utf-8 -*-
# Import necessary modules
import re # Regular expression module
import csv # CSV file reading and writing module
import os # Operating system module
# Define functions for domain checking and replacement
def contains_domain(address, domain):
  domain_pattern = r'[\w\.-]+@'+domain+'$' # Regular expression pattern for matching the domain
  if re.match(domain_pattern,address): # If the pattern matches, return True
    return True # Return True if the domain is found
  return False # Return False if the domain is not found
# Replace the old domain with the new domain in the email address
def replace_domain(address, old_domain, new_domain):
  old_domain_pattern = r'' + old_domain + '$' # Regular expression pattern for matching the old domain
  address = re.sub(old_domain_pattern, new_domain, address) # Replace the old domain with the new domain
  return address # Return the updated email address
# Main function to execute the script
def main():
  old_domain, new_domain = 'abc.edu', 'xyz.edu' # Define old and new domains
  csv_file_location = os.getcwd() + '/user_emails.csv' # Location of the input CSV file
  report_file = os.getcwd() + '/updated_user_emails.csv' # Location of the output CSV file
  user_email_list = [] # List to store user email addresses
  old_domain_email_list = [] # List to store email addresses with the old domain
  new_domain_email_list = [] # List to store email addresses with the new domain
 # Open the input CSV file for reading  
  with open(csv_file_location, 'r') as f:
    user_data_list = list(csv.reader(f)) # Read the CSV file into a list of lists
    user_email_list = [data[1].strip() for data in user_data_list[1:]] # Extract email addresses from the second column
    # Iterate through each email address
    for email_address in user_email_list: 
      if contains_domain(email_address, old_domain): # Check if the email address contains the old domain
        old_domain_email_list.append(email_address) # Add the email address to the old domain list
        replaced_email = replace_domain(email_address,old_domain,new_domain) # Replace the old domain with the new domain
        new_domain_email_list.append(replaced_email)  
    # Define the email key with a leading space
    email_key = ' ' + 'Email Address' 
    email_index = user_data_list[0].index(email_key) # Find the index of the email column
    # Iterate through each user in the data list (excluding header)
    for user in user_data_list[1:]: 
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list): # Iterate through old and new domain email lists
        if user[email_index] == ' ' + old_domain: # If the user's email matches the old domain email
          user[email_index] = ' ' + new_domain # Update the user's email to the new domain email
  f.close() # Close the input file
  # Open the output CSV file for writing
  with open(report_file, 'w+') as output_file:
    writer = csv.writer(output_file) # Create a CSV writer object
    writer.writerows(user_data_list) # Write the updated user data list to the output file
    output_file.close() # Close the output file   
# Call the main function to execute the script
main()