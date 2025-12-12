import csv # For CSV file handling
import re # For regular expressions
def contains_domain(address, domain): # Check if email address contains the given domain
  domain_pattern = r'[\w\.-]+@'+domain+'$' # Regex pattern to match the domain
  if re.match(domain_pattern, address): # If match found
    return True # Return True
  return False # Return False if no match found
def replace_domain(address, old_domain, new_domain): # Replace old domain with new domain in email address
  old_domain_pattern = r'' + old_domain + '$' # Regex pattern to match the old domain
  address = re.sub(old_domain_pattern, new_domain, address) # Replace old domain with new domain
  return address # Return updated email address
def main(): # Main function to read CSV, update emails, and write to new CSV
  csv_file_location = '<csv_file_location>' # Path to input CSV file
  report_file =  '<data-directory>' + '/updated_user_emails.csv' # Path to output CSV file
  user_email_list = [] # List to store user email addresses
  old_domain_email_list = [] # List to store email addresses with old domain
  new_domain_email_list = [] # List to store updated email addresses
  with open(csv_file_location, 'r') as f: # Open CSV file for reading
    user_data_list = list(csv.reader(f)) # Read CSV file into a list
    user_email_list = [data[1].strip() for data in user_data_list[1:]] # Extract email addresses from CSV
    