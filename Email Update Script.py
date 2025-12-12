#/usr/bin/ev python3

import csv # For CSV file handling
import re # For regular expressions

def contains_domain(address, domain): # Check if email address contains the specified domain
    domain_pattern = r'[\w\.-]+@'+domain+'$' # Regex pattern to match the domain
    if re.match(domain_pattern, address): # Match the pattern
        return True # Return True if match found
        return False # Return False if no match

def replace_domain(address, old_domain, new_domain): # Replace old domain with new domain in email address
    old_domain_pattern = r'' + old_domain + '$' # Regex pattern to match the old domain
    address = re.sub(old_domain_pattern, new_domain, address) # Replace old domain with new domain
    return address # Return updated email address

def main(): # Main function to read CSV, update emails, and write report
    old_domain, new_domain = 'abc.edu', 'xyz.edu' # Define old and new domains
    csv_file_location = '<csv_file_location>' # Path to input CSV file
    report_file =  '<data-directory>' + '/updated_user_emails.csv' # Path to output report file
    user_email_list = [] # List to store user emails
    old_domain_email_list = [] # List to store emails with old domain
    new_domain_email_list = [] # List to store updated emails

    with open(csv_file_location, 'r') as f: # Open CSV file for reading
        user_data_list = list(csv.reader(f)) # Read CSV file into a list
        user_email_list = [data[1].strip() for data in user_data_list[1:]] # Extract email addresses from CSV

    for email_address in user_email_list:
      if contains_domain(email_address, old_domain): # Check if email contains old domain
        old_domain_email_list.append(email_address) # Add to old domain email list
        replaced_email = replace_domain(email_address, old_domain, new_domain) # Replace old domain with new domain
        new_domain_email_list.append(replaced_email) # Add updated email to new domain email list

    email_key = ' ' + 'Email Address' # Define email column header
    email_index = user_data_list[0].index(email_key) # Get index of email column
    for user in user_data_list[1:]: # Iterate through user data
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list): # Zip old and new domain email lists
        if user[email_index] == ' ' + old_domain: # Check if user's email matches old domain email
          user[email_index] = ' ' + new_domain # Update user's email to new domain email
    f.close() # Close input file

    with open(report_file, 'w+') as output_file: # Open report file for writing
        writer = csv.writer(output_file) # Create CSV writer
        writer.writerows(user_data_list) # Write updated user data to report file
        output_file.close() # Close report file

main() # Call main function to execute the script
