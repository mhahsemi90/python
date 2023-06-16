import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape cryptocurrency information from CoinMarketCap
def scrape_crypto_info():
    # Send a GET request to the CoinMarketCap homepage
    url = 'https://coinmarketcap.com/'
    response = requests.get(url)

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the cryptocurrency information
    results_table = soup.find('table', {'class': 'cmc-table cmc-table___11lFC cmc-table-homepage___2_guh'})

    # Extract the cryptocurrency information as a list of dictionaries
    crypto_info_list = []
    for result in results_table.find_all('tr')[1:]:
        crypto_info = {}
        crypto_info['Rank'] = result.find('td', {'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__rank'}).text.strip()
        crypto_info['Name'] = result.find('a', {'class': 'cmc-link'}).text.strip()
        crypto_info['Symbol'] = result.find('div', {'class': 'cmc-table__column-name--symbol'}).text.strip()
        crypto_info['Price'] = result.find('td', {'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price'}).text.strip().replace('$', '')
        crypto_info['MarketCap'] = result.find('td', {'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap'}).text.strip().replace('$', '').replace(',', '')
        crypto_info['Volume'] = result.find('td', {'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__volume-24-h'}).text.strip().replace('$', '').replace(',', '')
        crypto_info['Change'] = result.find('td', {'class': 'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-24-h'}).text.strip().replace('%', '')
        crypto_info_list.append(crypto_info)

    # Return the list of cryptocurrency information
    return crypto_info_list

# Main function to run the script
def main():
    # Scrape cryptocurrency information from CoinMarketCap
    crypto_info_list = scrape_crypto_info()

    # Create a pandas DataFrame to store the cryptocurrency information
    df = pd.DataFrame(crypto_info_list)

    # Save the DataFrame to a CSV file
    df.to_csv('crypto_info.csv', index=False)

    # Print a message to confirm that the data was saved to the CSV file
    print('Cryptocurrency information saved to CSV file.')

# Call the main function
if __name__ == '__main__':
    main()