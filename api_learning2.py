import requests

def fetch_api():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        product_price = user_data["price"]
        product_rating = user_data["rating"]
        return product_price,product_rating
    else:
        raise Exception("Api not fetched properly")
    
    def main():
        try:
            product_price,product_rating = fetch_api()
            print("Product_Price:{product_price}\nProduct_Rating:{product_rating}")
        except Exception as e:
            print(str(e))
        
        
        if __name__ == "__main__":
            main()
        
        
        
    
    