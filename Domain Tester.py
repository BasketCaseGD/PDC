import requests

def check_domain(domain):
    try:
        response = requests.get(f"http://{domain}", timeout=5)
        if response.status_code == 200:
            return True
    except requests.RequestException:
        return False
    return False

def process_domains(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        domains = infile.readlines()
        for domain in domains:
            domain = domain.strip()
            if check_domain(domain):
                print(f"{domain} is online")
                outfile.write(domain + "\n")
            else:
                print(f"{domain} is offline")

if __name__ == "__main__":
    input_file = input("Enter the path to the input text file: ")
    output_file = input("Enter the path to the output text file: ")
    process_domains(input_file, output_file)
    print("Process complete. Working domains have been written to the output file.")
