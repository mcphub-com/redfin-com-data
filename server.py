import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

__rapidapi_url__ = 'https://rapidapi.com/ntd119/api/redfin-com-data'

mcp = FastMCP('redfin-com-data')

@mcp.tool()
def properties_auto_complete(query: Annotated[str, Field(description='Required: true Ex: New York')],
                             limit: Annotated[Union[int, float, None], Field(description='Total number of record per api call It has a value ranging from 1 to 50 Ex: 2 Default: 25')] = None) -> dict: 
    '''properties/auto-complete'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/auto-complete'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_search_sale(regionId: Annotated[str, Field(description="Use the 'page' parameter to get the full data until 'moreData=false Description for endpoint: Search properties for sale Required: true regionId can be retrieved from /properties/auto-complete endpoint(data->rows->id) Ex: 6_2446 (Camas, WA, USA)")],
                           limit: Annotated[Union[int, float, None], Field(description='Total number of record per api call It has a value ranging from 1 to 1000 Ex: 100 Default: 350 Default: 0')] = None,
                           page: Annotated[Union[int, float, None], Field(description='The page index, for paging purpose Ex: 2 Default value: 1 Default: 0')] = None,
                           prices: Annotated[Union[str, None], Field(description='Prices Min and max prices should be separated by commas Ex: 50000,350000 In the case of only having the minimum price: Ex: 50000 In the case of only having the maximum price: Ex: ,350000 In case of having both: Ex: 50000,350000')] = None,
                           beds: Annotated[Union[int, float, None], Field(description='Bedroom Default value: No min Choose one of the values below 1: 1+ 2: 2+ 3: 3+ 4: 4+ 5: 5+ 6: 6+ Default: 0')] = None,
                           baths: Annotated[Union[int, float, None], Field(description='Bathroom Default value: No min Choose one of the values below 1: 1+ 1.5: 1.5+ 2: 2+ 2.5: 2.5+ 3: 3+ 4: 4+ 5: 5+ 6: 6+ Default: 0')] = None,
                           homeType: Annotated[Union[str, None], Field(description='Home type It can input multiple values, and the values should be separated by commas Ex: 1,3 Default value: Select all 1: House 3: Townhouse 2: Condo 4: Multi-family 7: Manufactured 8: Co-op 5: Land 6: Other')] = None,
                           squareFeet: Annotated[Union[str, None], Field(description='Square feet Min and max prices should be separated by commas Ex: 500,1000 In the case of only having the minimum square feet: Ex: 500 In the case of only having the maximum square feet: Ex: ,1000 In case of having both: Ex: 500,1000 500: 500 750: 500 1000: 1000 ...........')] = None,
                           lotSize: Annotated[Union[str, None], Field(description='Lot size Min and max prices should be separated by commas Ex: 2000,8000 In the case of only having the minimum lot size: Ex: 2000 In the case of only having the maximum lot size: Ex: ,8000 In case of having both: Ex: 2000,8000 2000: 2,000 sq. ft. 4500: 4,500 sq. ft. 6500: 6,500 sq. ft. 8000: 8,000 sq. ft. 10890: 0.25 acres 21780: 0.5 acres 43560: 1 acre 87120: 2 acres ................')] = None,
                           status: Annotated[Union[int, float, None], Field(description='Status Ex: 9 Default: 9 Choose one of the values below 9: Active+coming soon 1: Active listings 8: Coming soon 131: Active + under contract/pending 130: Only under contract/pending Default: 0')] = None,
                           timeOnRedfin: Annotated[Union[str, None], Field(description='Time On Redfin Ex: - Default: - Choose one of the values below -: Any 1-: Less than 1 day 3-: Less than 3 days ...................... -7: More than 7 days -14: More than 14 days ......................')] = None,
                           stories: Annotated[Union[str, None], Field(description='Stories Min and max stories should be separated by commas Default minimum stories is 1 Ex: 1,3 In the case of only having the minimum stories: Ex: 1 In the case of only having the maximum stories: Ex: ,3 In case of having both: Ex: 1,3')] = None,
                           yearBuilt: Annotated[Union[str, None], Field(description='Year built Min and max year built should be separated by commas Ex: 2009,2012 In the case of only having the minimum year built: Ex: 2009 In the case of only having the maximum year built: Ex: ,2012 In case of having both: Ex: 2009,2012 1900: 1900 1910: 1910 ............')] = None,
                           booleanFilters: Annotated[Union[str, None], Field(description='Used in case the items have true/false values on Redfin It can input multiple values, and the values should be separated by commas Ex: fixer,excl_ar fixer: Fixer-upper excl_ar: Exclude 55+ communities include_outdoor_parking: Include outdoor parking rv_parking: RV parking ac: Air conditioning fireplace: Fireplace primary_bed_on_main: Primary bedroom on main floor wf: Waterfront view: Has view basement_finished: Basement finished basement_unfinished: Basement unfinished pets_allowed: Pets allowed wd: Washer/dryer hookup guest_house: Guest house accessible: Accessible home elevator: Elevator green: Green home excl_ll: Exclude land leases excl_ss: Exclude short sales unrated_schools: Include unrated schools virtual_tour: 3D & video tour')] = None,
                           pool: Annotated[Union[int, float, None], Field(description='Pool Ex: 1 Choose one of the values below 1: Private pool 2: Community pool 3: Private or community pool 4: No private pool Default: 0')] = None,
                           garageSpots: Annotated[Union[int, float, None], Field(description='Garage spots Ex: 1 Choose one of the values below 1: 1+ 2: 2+ 3: 3+ 4: 4+ 5: 5+ Default: 0')] = None,
                           hoaFees: Annotated[Union[int, float, None], Field(description='HOA fees Ex: 0 Choose one of the values below 0: No Hoa 25: $25/month 50: $50/month 75: $75/month ............... Default: 0')] = None,
                           priceSqft: Annotated[Union[str, None], Field(description='Price/Sq. Ft. Min and max price/Sq. Ft should be separated by commas Ex: 100,250 In the case of only having the minimum price/Sq. Ft: Ex: 100 In the case of only having the maximum price/Sq. Ft: Ex: ,250 In case of having both: Ex: 100,250 50: 50 100: 100 150: 150 200: 200 ............')] = None,
                           propertyTaxes: Annotated[Union[int, float, None], Field(description='Property taxes Ex: 250 Choose one of the values below 250: $250/year 500: $500/year 750: $750/year 1000: $1000/year ............... Default: 0')] = None,
                           acceptedFinancing: Annotated[Union[int, float, None], Field(description='Accepted financing Ex: 1 Choose one of the values below 1: FHA 2: VA Default: 0')] = None,
                           priceReduced: Annotated[Union[str, None], Field(description='Price reduced Ex: 1- Choose one of the values below 1-: Less than 1 day 3-: Less than 3 days 7-: Less than 7 days 14-: Less than 14 days 30-: Less than 30 days -30: More than 30 days -60: More than 60 days -120: More than 120 days -: Any time')] = None,
                           listingType: Annotated[Union[str, None], Field(description='Listing type It can input multiple values, and the values should be separated by commas Ex: 1,2,3,4,5,6,7 Default value: 1,2,3,4,5,6,7 - Turn on MLS listings select all and select For Sale By Owner, Foreclosures 5,6: New construction 1,7: By agent 2: MLS-Listed Foreclosures 3: For Sale By Owner 4: Foreclosures')] = None,
                           greatSchoolsRating: Annotated[Union[int, float, None], Field(description='GreatSchools rating Ex: 1 Choose one of the values below 1: 1+ 2: 2+ ........ 10: 10 Default: 0')] = None,
                           schoolTypes: Annotated[Union[str, None], Field(description='School types Default value: 2 when select greatSchoolsRating Ex: 1 Choose one of the values below 1: Elementary school 2: Middle school 3: High school')] = None,
                           walkScore: Annotated[Union[int, float, None], Field(description='Walk Score Ex: 10 Choose one of the values below 10: 10+ 20: 20+ ........ 90: 90+ Default: 0')] = None,
                           transitScore: Annotated[Union[int, float, None], Field(description='Transit Score Ex: 10 Choose one of the values below 10: 10+ 20: 20+ ........ 90: 90+ Default: 0')] = None,
                           bikeScore: Annotated[Union[int, float, None], Field(description='Bike Score Ex: 30 Choose one of the values below 10: 10+ 20: 20+ ........ 90: 90+ Default: 0')] = None,
                           openHouse: Annotated[Union[int, float, None], Field(description='Open house Ex: 1 Choose one of the values below 1: Any time 2: This weekend Default: 0')] = None,
                           keyword: Annotated[Union[str, None], Field(description='Keyword search: e.g. office, balcony, modern Ex: office')] = None) -> dict: 
    '''Search properties for sale'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/search-sale'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'regionId': regionId,
        'limit': limit,
        'page': page,
        'prices': prices,
        'beds': beds,
        'baths': baths,
        'homeType': homeType,
        'squareFeet': squareFeet,
        'lotSize': lotSize,
        'status': status,
        'timeOnRedfin': timeOnRedfin,
        'stories': stories,
        'yearBuilt': yearBuilt,
        'booleanFilters': booleanFilters,
        'pool': pool,
        'garageSpots': garageSpots,
        'hoaFees': hoaFees,
        'priceSqft': priceSqft,
        'propertyTaxes': propertyTaxes,
        'acceptedFinancing': acceptedFinancing,
        'priceReduced': priceReduced,
        'listingType': listingType,
        'greatSchoolsRating': greatSchoolsRating,
        'schoolTypes': schoolTypes,
        'walkScore': walkScore,
        'transitScore': transitScore,
        'bikeScore': bikeScore,
        'openHouse': openHouse,
        'keyword': keyword,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_search_rent(regionId: Annotated[str, Field(description='Description for endpoint: Search properties for rent Prices Min and max prices should be separated by commas Ex: 400,2100 In the case of only having the minimum price: Ex: 400 In the case of only having the maximum price: Ex: ,2100 In case of having both: Ex: 400,2100')],
                           prices: Annotated[Union[str, None], Field(description='Prices Min and max prices should be separated by commas Ex: 400,2100 In the case of only having the minimum price: Ex: 400 In the case of only having the maximum price: Ex: ,2100 In case of having both: Ex: 400,2100')] = None,
                           beds: Annotated[Union[int, float, None], Field(description='Bedroom Default value: No min Choose one of the values below 1: 1+ 2: 2+ 3: 3+ 4: 4+ 5: 5+ 6: 6+ Default: 0')] = None,
                           baths: Annotated[Union[int, float, None], Field(description='Bathroom Default value: No min Choose one of the values below 1: 1+ 1.5: 1.5+ 2: 2+ 2.5: 2.5+ 3: 3+ 4: 4+ 5: 5+ 6: 6+ Default: 0')] = None,
                           homeType: Annotated[Union[str, None], Field(description='Home type It can input multiple values, and the values should be separated by commas Ex: 1,3 Default value: Select all 1: House 4: Apartment 3: Townhouse 2: Condo')] = None,
                           moveInDate: Annotated[Union[str, None], Field(description='Move in date Format: YYYY-MM-DD Ex: 2024-03-21')] = None,
                           squareFeet: Annotated[Union[str, None], Field(description='Square feet Min and max prices should be separated by commas Ex: 500,1000 In the case of only having the minimum square feet: Ex: 500 In the case of only having the maximum square feet: Ex: ,1000 In case of having both: Ex: 500,1000 500: 500 750: 500 1000: 1000 ...........')] = None,
                           lotSize: Annotated[Union[str, None], Field(description='Lot size Min and max prices should be separated by commas Ex: 2000,8000 In the case of only having the minimum lot size: Ex: 2000 In the case of only having the maximum lot size: Ex: ,8000 In case of having both: Ex: 2000,8000 2000: 2,000 sq. ft. 4500: 4,500 sq. ft. 6500: 6,500 sq. ft. 8000: 8,000 sq. ft. 10890: 0.25 acres 21780: 0.5 acres 43560: 1 acre 87120: 2 acres ................')] = None,
                           status: Annotated[Union[int, float, None], Field(description='Status Ex: 9 Default: 9 Choose one of the values below 9: Active+coming soon 1: Active listings 8: Coming soon 131: Active + under contract/pending 130: Only under contract/pending Default: 0')] = None,
                           timeOnRedfin: Annotated[Union[str, None], Field(description='Time On Redfin Ex: - Default: - Choose one of the values below -: Any 1-: Less than 1 day 3-: Less than 3 days ...................... -7: More than 7 days -14: More than 14 days ......................')] = None,
                           stories: Annotated[Union[str, None], Field(description='Stories Min and max stories should be separated by commas Default minimum stories is 1 Ex: 1,3 In the case of only having the minimum stories: Ex: 1 In the case of only having the maximum stories: Ex: ,3 In case of having both: Ex: 1,3')] = None,
                           yearBuilt: Annotated[Union[str, None], Field(description='Year built Min and max year built should be separated by commas Ex: 2009,2012 In the case of only having the minimum year built: Ex: 2009 In the case of only having the maximum year built: Ex: ,2012 In case of having both: Ex: 2009,2012 1900: 1900 1910: 1910 ............')] = None,
                           booleanFilters: Annotated[Union[str, None], Field(description='Used in case the items have true/false values on Redfin It can input multiple values, and the values should be separated by commas Ex: has_deal,dogs_allowed,cats_allowed has_deal: Deals - Only show listings with deals or promotions dogs_allowed: Dogs allowed cats_allowed: Cats allowed has_ac: Air conditioning has_in_unit_laundry: In-unit washer and dryer has_laundry_facility: Laundry facility has_laundry_hookups: Washer/dryer hookups has_dishwasher: Dishwasher has_parking: Parking allowed utilities_included: Utilities included is_furnished: Furnished has_pool: Pool is_income_restricted: Income restricted is_senior_living: Senior living has_short_term_lease: Short term has_virtual_tour: 3D & video tour')] = None,
                           greatSchoolsRating: Annotated[Union[int, float, None], Field(description='GreatSchools rating Ex: 1 Choose one of the values below 1: 1+ 2: 2+ ........ 10: 10 Default: 0')] = None,
                           schoolTypes: Annotated[Union[str, None], Field(description='School types Default value: 2 when select greatSchoolsRating Ex: 1 Choose one of the values below 1: Elementary school 2: Middle school 3: High school')] = None,
                           walkScore: Annotated[Union[int, float, None], Field(description='Walk Score Ex: 10 Choose one of the values below 10: 10+ 20: 20+ ........ 90: 90+ Default: 0')] = None,
                           transitScore: Annotated[Union[int, float, None], Field(description='Transit Score Ex: 10 Choose one of the values below 10: 10+ 20: 20+ ........ 90: 90+ Default: 0')] = None,
                           bikeScore: Annotated[Union[int, float, None], Field(description='Bike Score Ex: 30 Choose one of the values below 10: 10+ 20: 20+ ........ 90: 90+ Default: 0')] = None) -> dict: 
    '''Search properties for rent'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/search-rent'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'regionId': regionId,
        'prices': prices,
        'beds': beds,
        'baths': baths,
        'homeType': homeType,
        'moveInDate': moveInDate,
        'squareFeet': squareFeet,
        'lotSize': lotSize,
        'status': status,
        'timeOnRedfin': timeOnRedfin,
        'stories': stories,
        'yearBuilt': yearBuilt,
        'booleanFilters': booleanFilters,
        'greatSchoolsRating': greatSchoolsRating,
        'schoolTypes': schoolTypes,
        'walkScore': walkScore,
        'transitScore': transitScore,
        'bikeScore': bikeScore,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_search_by_url(url: Annotated[str, Field(description='URL get properties Ex: https://www.redfin.com/city/30749/NY/New-York')]) -> dict: 
    '''Search properties by url'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/search-by-url'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_get_listingid(propertyId: Annotated[str, Field(description='Required: true propertyId can be retrieved from /properties/auto-complete endpoint(data->rows->propertyId) At /auto-complete endpoint: Note that the propertyId only appears when the location is an address Ex: 29171311')]) -> dict: 
    '''Get listingId for detais'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/get-listingId'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'propertyId': propertyId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_details(url: Annotated[str, Field(description='Required: true The url can be retrieved from below endpoint(data->homeData->url) /properties/search-sale /properties/search-rent /properties/search-sold /properties/search-by-url (data->homes->url) Ex: /WA/Camas/3636-NW-24th-Cir-98607/home/18426094')]) -> dict: 
    '''properties/details'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/details'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_detail_by_url(url: Annotated[str, Field(description='URL to get detail Required: true Ex: https://www.redfin.com/CT/New-Haven/Pierpont/apartment/176060870')]) -> dict: 
    '''properties/detail-by-url'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/detail-by-url'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_main_info(propertyId: Annotated[str, Field(description='Required: true propertyId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->propertyId)')],
                         listingId: Annotated[Union[str, None], Field(description='Required: true listingId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->listingId) Ex: 138238059')] = None) -> dict: 
    '''Get main info of a property'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/main-info'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'propertyId': propertyId,
        'listingId': listingId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_extra_info(propertyId: Annotated[str, Field(description='Required: true propertyId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->propertyId)')],
                          listingId: Annotated[Union[str, None], Field(description='Required: true listingId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->listingId) Ex: 138238059')] = None) -> dict: 
    '''Get extra info of a property'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/extra-info'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'propertyId': propertyId,
        'listingId': listingId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_walk_score(propertyId: Annotated[str, Field(description='Required: true propertyId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->propertyId)')]) -> dict: 
    '''Get walk score of a property'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/walk-score'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'propertyId': propertyId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_amenities(propertyId: Annotated[str, Field(description='Required: true propertyId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->propertyId)')],
                         listingId: Annotated[Union[str, None], Field(description='Required: true listingId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->listingId) Ex: 138238059')] = None) -> dict: 
    '''Get all amenities of a property'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/amenities'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'propertyId': propertyId,
        'listingId': listingId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_get_agent(propertyId: Annotated[str, Field(description='Required: true propertyId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->propertyId)')],
                         listingId: Annotated[Union[str, None], Field(description='Required: true listingId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->listingId) Ex: 138238059')] = None) -> dict: 
    '''Get agent info relating to a property'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/get-agent'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'propertyId': propertyId,
        'listingId': listingId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_mortgage_calculator(propertyId: Annotated[str, Field(description='Required: true propertyId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->propertyId)')],
                                   listingId: Annotated[Union[str, None], Field(description='Required: true listingId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->listingId) Ex: 138238059')] = None) -> dict: 
    '''Get mortgage calculator of a property'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/mortgage-calculator'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'propertyId': propertyId,
        'listingId': listingId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_estimate(propertyId: Annotated[str, Field(description='Required: true propertyId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->propertyId)')],
                        listingId: Annotated[Union[str, None], Field(description='Required: true listingId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->listingId) Ex: 138238059')] = None) -> dict: 
    '''Get Redfin's estimate of a property'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/estimate'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'propertyId': propertyId,
        'listingId': listingId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_tour_insights(propertyId: Annotated[str, Field(description='Required: true propertyId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->propertyId)')],
                             listingId: Annotated[Union[str, None], Field(description='Required: true listingId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->listingId) Ex: 138238059')] = None) -> dict: 
    '''Get tour insights of a property'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/tour-insights'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'propertyId': propertyId,
        'listingId': listingId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_popularity_info(listingId: Annotated[str, Field(description='Required: true listingId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->listingId) Ex: 138238059')]) -> dict: 
    '''Get popularity info relating to a property'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/popularity-info'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'listingId': listingId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_parcel_bounds(propertyId: Annotated[str, Field(description='Required: true propertyId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->propertyId)')]) -> dict: 
    '''Get parcel bounds info. This endpoint is used to get fipsCode and apn to pass in /properties/flood-info endpoint.'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/parcel-bounds'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'propertyId': propertyId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_coordinates(propertyId: Annotated[str, Field(description='Required: true propertyId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->propertyId)')]) -> dict: 
    '''Get coordinates. This endpoint is used to get lat and lng to pass in /properties/flood-info endpoint.'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/coordinates'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'propertyId': propertyId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_flood_info(fipsCode: Annotated[str, Field(description='Required: true fipsCode can be retrieved from /properties/parcel-bounds endpoint(data->fipsCode) Ex: 53011')],
                          apn: Annotated[str, Field(description='Required: true apn can be retrieved from /properties/parcel-bounds endpoint(data->apn) Ex: 011-986056496')],
                          lat: Annotated[str, Field(description='The latitude of GEO location Required: true lat can be retrieved from /properties/coordinates endpoint(data->lat) Ex: 45.681162')],
                          lng: Annotated[str, Field(description='The longitude of GEO location Required: true lng can be retrieved from /properties/coordinates endpoint(data->lng) Ex: -122.314572')]) -> dict: 
    '''Get flood info'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/flood-info'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fipsCode': fipsCode,
        'apn': apn,
        'lat': lat,
        'lng': lng,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_date_picker_data(listingId: Annotated[str, Field(description='Required: true listingId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->listingId) Ex: 138238059')]) -> dict: 
    '''Get all schedule tour of a property'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/date-picker-data'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'listingId': listingId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_customer_conversion_info(propertyId: Annotated[str, Field(description='Required: true propertyId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->propertyId)')],
                                        listingId: Annotated[Union[str, None], Field(description='Required: true listingId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->listingId) Ex: 138238059')] = None) -> dict: 
    '''Get customer conversion info'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/customer-conversion-info'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'propertyId': propertyId,
        'listingId': listingId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_price_drop_info(listingId: Annotated[str, Field(description='Required: true listingId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->listingId) Ex: 183460396')]) -> dict: 
    '''Get price drop info a property'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/price-drop-info'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'listingId': listingId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_hot_market_info(propertyId: Annotated[str, Field(description='Required: true propertyId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->propertyId)')]) -> dict: 
    '''Get hot market info'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/hot-market-info'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'propertyId': propertyId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def properties_main_house_info_panel_info(propertyId: Annotated[str, Field(description='Required: true propertyId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->propertyId)')],
                                          listingId: Annotated[Union[str, None], Field(description='Required: true listingId can be retrieved from /properties/search-sale or /properties/search-rent or /properties/search-sold endpoint(data->homeData->listingId) Ex: 138238059')] = None) -> dict: 
    '''Get main house info panel info'''
    url = 'https://redfin-com-data.p.rapidapi.com/properties/main-house-info-panel-info'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'propertyId': propertyId,
        'listingId': listingId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def autocomplete(location: Annotated[str, Field(description='')]) -> dict: 
    '''Autocomplete'''
    url = 'https://redfin-com-data.p.rapidapi.com/property/auto-complete'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search(location: Annotated[str, Field(description='Address or zip code location can be retrieved from /property/auto-complete endpoint(data->sections->rows->name)')],
           sub_location: Annotated[Union[str, None], Field(description='sub_location can be retrieved from /property/auto-complete endpoint(data->sections->rows->subName)')] = None,
           page: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           search_by: Annotated[Union[str, None], Field(description='Choose one of the values below places schools agents buildings addresses Default: places')] = None,
           sort: Annotated[Union[str, None], Field(description='Choose one of the values below Recommended Newest PriceLowToHigh PriceHighToLow SquareFeet LotSize PriceSqft')] = None,
           search_type: Annotated[Union[str, None], Field(description='Choose one of the values below Sold ForSale Default: ForSale')] = None,
           sold_within: Annotated[Union[str, None], Field(description='This option only has an available when search_type=Sold Choose one of the values below Last-1Week Last-1Month Last-3Months Last-6Months Last-1Year Last-2Years Last-3Years Last-5Years Default: Last-3Months')] = None,
           min_price: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           max_price: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           home_type: Annotated[Union[str, None], Field(description='Property type comma-separated or empty for all types: House Townhouse Condo Land MultiFamily Mobile Co-op Other Ex: House,Townhouse')] = None,
           min_bedroom: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           max_bedroom: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           min_bathroom: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           status: Annotated[Union[str, None], Field(description='Choose one of the values below ComingSoon Active')] = None,
           time_on_redfin: Annotated[Union[str, None], Field(description='Choose one of the values below NewListings LessThan3Days LessThan7Days LessThan14Days LessThan30Days MoreThan7Days MoreThan14Days MoreThan30Days MoreThan45Days MoreThan60Days MoreThan90Days MoreThan180Days')] = None,
           min_square_feet: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           max_square_feet: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           min_lot_size: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           max_lot_size: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           min_stories: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           max_stories: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           min_year_built: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           max_year_built: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
           has_exclude_55_communities: Annotated[Union[bool, None], Field(description='')] = None,
           garage_spots: Annotated[Union[int, float, None], Field(description='garage_spots: 1->5 Default: 0')] = None,
           pool_type: Annotated[Union[str, None], Field(description='Choose one of the values below PrivatePool CommunityPool PrivateOrCommunityPool NoPrivatePool')] = None,
           has_include_outdoor_parking: Annotated[Union[bool, None], Field(description='')] = None,
           has_air_conditioning: Annotated[Union[bool, None], Field(description='')] = None,
           has_waterfront: Annotated[Union[bool, None], Field(description='')] = None,
           has_view: Annotated[Union[bool, None], Field(description='')] = None,
           has_fireplace: Annotated[Union[bool, None], Field(description='')] = None,
           has_fixer_upper: Annotated[Union[bool, None], Field(description='')] = None,
           has_guest_house: Annotated[Union[bool, None], Field(description='')] = None,
           has_elevator: Annotated[Union[bool, None], Field(description='')] = None,
           has_basement: Annotated[Union[bool, None], Field(description='')] = None,
           has_washer_dryer_hookup: Annotated[Union[bool, None], Field(description='')] = None,
           has_pets_allowed: Annotated[Union[bool, None], Field(description='')] = None,
           has_primary_bedroom_on_main_floor: Annotated[Union[bool, None], Field(description='')] = None,
           has_rv_parking: Annotated[Union[bool, None], Field(description='')] = None,
           has_green_home: Annotated[Union[bool, None], Field(description='')] = None,
           has_accessible_home: Annotated[Union[bool, None], Field(description='')] = None,
           keyword_search: Annotated[Union[str, None], Field(description='')] = None,
           listing_type: Annotated[Union[str, None], Field(description='Multiple values can be entered and comma-separated Ex: ByAgent,ByOwner ByAgent: By agent ByOwner: By owner (FSBO) NewConstruction: New construction Foreclosures: Foreclosures')] = None) -> dict: 
    '''Search'''
    url = 'https://redfin-com-data.p.rapidapi.com/property/search'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
        'sub_location': sub_location,
        'page': page,
        'search_by': search_by,
        'sort': sort,
        'search_type': search_type,
        'sold_within': sold_within,
        'min_price': min_price,
        'max_price': max_price,
        'home_type': home_type,
        'min_bedroom': min_bedroom,
        'max_bedroom': max_bedroom,
        'min_bathroom': min_bathroom,
        'status': status,
        'time_on_redfin': time_on_redfin,
        'min_square_feet': min_square_feet,
        'max_square_feet': max_square_feet,
        'min_lot_size': min_lot_size,
        'max_lot_size': max_lot_size,
        'min_stories': min_stories,
        'max_stories': max_stories,
        'min_year_built': min_year_built,
        'max_year_built': max_year_built,
        'has_exclude_55_communities': has_exclude_55_communities,
        'garage_spots': garage_spots,
        'pool_type': pool_type,
        'has_include_outdoor_parking': has_include_outdoor_parking,
        'has_air_conditioning': has_air_conditioning,
        'has_waterfront': has_waterfront,
        'has_view': has_view,
        'has_fireplace': has_fireplace,
        'has_fixer_upper': has_fixer_upper,
        'has_guest_house': has_guest_house,
        'has_elevator': has_elevator,
        'has_basement': has_basement,
        'has_washer_dryer_hookup': has_washer_dryer_hookup,
        'has_pets_allowed': has_pets_allowed,
        'has_primary_bedroom_on_main_floor': has_primary_bedroom_on_main_floor,
        'has_rv_parking': has_rv_parking,
        'has_green_home': has_green_home,
        'has_accessible_home': has_accessible_home,
        'keyword_search': keyword_search,
        'listing_type': listing_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_rent(location: Annotated[str, Field(description='Address or zip code location can be retrieved from /property/auto-complete endpoint(data->sections->rows->name)')],
                sub_location: Annotated[Union[str, None], Field(description='sub_location can be retrieved from /property/auto-complete endpoint(data->sections->rows->subName)')] = None,
                page: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                search_by: Annotated[Union[str, None], Field(description='Choose one of the values below places schools agents buildings addresses Default: places')] = None,
                sort: Annotated[Union[str, None], Field(description='Choose one of the values below Recommended Newest PriceLowToHigh PriceHighToLow SquareFeet LotSize PriceSqft')] = None,
                sold_within: Annotated[Union[str, None], Field(description='This option only has an available when search_type=Sold Choose one of the values below Last-1Week Last-1Month Last-3Months Last-6Months Last-1Year Last-2Years Last-3Years Last-5Years Default: Last-3Months')] = None,
                min_price: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                max_price: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                home_type: Annotated[Union[str, None], Field(description='Property type comma-separated or empty for all types: House Townhouse Condo Land MultiFamily Mobile Co-op Other Ex: House,Townhouse')] = None,
                min_bedroom: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                max_bedroom: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                min_bathroom: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                status: Annotated[Union[str, None], Field(description='Choose one of the values below ComingSoon Active')] = None,
                move_in_date: Annotated[Union[str, datetime, None], Field(description='Choose one of the values below NewListings LessThan3Days LessThan7Days LessThan14Days LessThan30Days MoreThan7Days MoreThan14Days MoreThan30Days MoreThan45Days MoreThan60Days MoreThan90Days MoreThan180Days')] = None,
                min_square_feet: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                max_square_feet: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                min_lot_size: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                max_lot_size: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                min_stories: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                max_stories: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                min_year_built: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                max_year_built: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
                has_exclude_55_communities: Annotated[Union[bool, None], Field(description='')] = None,
                garage_spots: Annotated[Union[int, float, None], Field(description='garage_spots: 1->5 Default: 0')] = None,
                pool_type: Annotated[Union[str, None], Field(description='Choose one of the values below PrivatePool CommunityPool PrivateOrCommunityPool NoPrivatePool')] = None,
                has_include_outdoor_parking: Annotated[Union[bool, None], Field(description='')] = None,
                has_air_conditioning: Annotated[Union[bool, None], Field(description='')] = None,
                has_waterfront: Annotated[Union[bool, None], Field(description='')] = None,
                has_view: Annotated[Union[bool, None], Field(description='')] = None,
                has_fireplace: Annotated[Union[bool, None], Field(description='')] = None,
                has_fixer_upper: Annotated[Union[bool, None], Field(description='')] = None,
                has_guest_house: Annotated[Union[bool, None], Field(description='')] = None,
                has_elevator: Annotated[Union[bool, None], Field(description='')] = None,
                has_basement: Annotated[Union[bool, None], Field(description='')] = None,
                has_washer_dryer_hookup: Annotated[Union[bool, None], Field(description='')] = None,
                has_pets_allowed: Annotated[Union[bool, None], Field(description='')] = None,
                has_primary_bedroom_on_main_floor: Annotated[Union[bool, None], Field(description='')] = None,
                has_rv_parking: Annotated[Union[bool, None], Field(description='')] = None,
                has_green_home: Annotated[Union[bool, None], Field(description='')] = None,
                has_accessible_home: Annotated[Union[bool, None], Field(description='')] = None,
                keyword_search: Annotated[Union[str, None], Field(description='')] = None,
                listing_type: Annotated[Union[str, None], Field(description='Multiple values can be entered and comma-separated Ex: ByAgent,ByOwner ByAgent: By agent ByOwner: By owner (FSBO) NewConstruction: New construction Foreclosures: Foreclosures')] = None) -> dict: 
    '''search-rent'''
    url = 'https://redfin-com-data.p.rapidapi.com/property/search-rent'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
        'sub_location': sub_location,
        'page': page,
        'search_by': search_by,
        'sort': sort,
        'sold_within': sold_within,
        'min_price': min_price,
        'max_price': max_price,
        'home_type': home_type,
        'min_bedroom': min_bedroom,
        'max_bedroom': max_bedroom,
        'min_bathroom': min_bathroom,
        'status': status,
        'move_in_date': move_in_date,
        'min_square_feet': min_square_feet,
        'max_square_feet': max_square_feet,
        'min_lot_size': min_lot_size,
        'max_lot_size': max_lot_size,
        'min_stories': min_stories,
        'max_stories': max_stories,
        'min_year_built': min_year_built,
        'max_year_built': max_year_built,
        'has_exclude_55_communities': has_exclude_55_communities,
        'garage_spots': garage_spots,
        'pool_type': pool_type,
        'has_include_outdoor_parking': has_include_outdoor_parking,
        'has_air_conditioning': has_air_conditioning,
        'has_waterfront': has_waterfront,
        'has_view': has_view,
        'has_fireplace': has_fireplace,
        'has_fixer_upper': has_fixer_upper,
        'has_guest_house': has_guest_house,
        'has_elevator': has_elevator,
        'has_basement': has_basement,
        'has_washer_dryer_hookup': has_washer_dryer_hookup,
        'has_pets_allowed': has_pets_allowed,
        'has_primary_bedroom_on_main_floor': has_primary_bedroom_on_main_floor,
        'has_rv_parking': has_rv_parking,
        'has_green_home': has_green_home,
        'has_accessible_home': has_accessible_home,
        'keyword_search': keyword_search,
        'listing_type': listing_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_v2(locationId: Annotated[str, Field(description='Address or zip code locationId can be retrieved from /property/auto-complete endpoint(data->sections->rows->idV2) Ex: eyJpIjogIjJfMzA4MTgiLCAidCI6ICJQbGFjZXMiLCAidSI6ICIvY2l0eS8zMDgxOC9UWC9BdXN0aW4ifQ==')],
              page: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
              search_by: Annotated[Union[str, None], Field(description='Choose one of the values below places schools agents buildings addresses Default: places')] = None,
              sort: Annotated[Union[str, None], Field(description='Choose one of the values below Recommended Newest PriceLowToHigh PriceHighToLow SquareFeet LotSize PriceSqft')] = None,
              search_type: Annotated[Union[str, None], Field(description='Choose one of the values below Sold ForRent ForSale Default: ForSale')] = None,
              sold_within: Annotated[Union[str, None], Field(description='This option only has an available when search_type=Sold Choose one of the values below Last-1Week `Last-1Month`` Last-3Months Last-6Months Last-1Year Last-2Years Last-3Years Last-5Years Default: Last-3Months')] = None,
              min_price: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
              max_price: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
              home_type: Annotated[Union[str, None], Field(description='Property type comma-separated or empty for all types: House Townhouse Condo Land MultiFamily Mobile Co-op Other Ex: House,Townhouse')] = None,
              min_bedroom: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
              max_bedroom: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
              min_bathroom: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
              status: Annotated[Union[str, None], Field(description='Choose one of the values below ComingSoon Active')] = None,
              time_on_redfin: Annotated[Union[str, None], Field(description='Choose one of the values below NewListings LessThan3Days LessThan7Days LessThan14Days LessThan30Days MoreThan7Days MoreThan14Days MoreThan30Days MoreThan45Days MoreThan60Days MoreThan90Days MoreThan180Days')] = None,
              min_square_feet: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
              max_square_feet: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
              min_lot_size: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
              max_lot_size: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
              min_stories: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
              max_stories: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
              min_year_built: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
              max_year_built: Annotated[Union[int, float, None], Field(description='Default: 0')] = None,
              has_exclude_55_communities: Annotated[Union[bool, None], Field(description='')] = None,
              garage_spots: Annotated[Union[int, float, None], Field(description='garage_spots: 1->5 Default: 0')] = None,
              pool_type: Annotated[Union[str, None], Field(description='Choose one of the values below PrivatePool CommunityPool PrivateOrCommunityPool NoPrivatePool')] = None,
              has_include_outdoor_parking: Annotated[Union[bool, None], Field(description='')] = None,
              has_air_conditioning: Annotated[Union[bool, None], Field(description='')] = None,
              has_waterfront: Annotated[Union[bool, None], Field(description='')] = None,
              has_view: Annotated[Union[bool, None], Field(description='')] = None,
              has_fireplace: Annotated[Union[bool, None], Field(description='')] = None,
              has_fixer_upper: Annotated[Union[bool, None], Field(description='')] = None,
              has_guest_house: Annotated[Union[bool, None], Field(description='')] = None,
              has_elevator: Annotated[Union[bool, None], Field(description='')] = None,
              has_basement: Annotated[Union[bool, None], Field(description='')] = None,
              has_washer_dryer_hookup: Annotated[Union[bool, None], Field(description='')] = None,
              has_pets_allowed: Annotated[Union[bool, None], Field(description='')] = None,
              has_primary_bedroom_on_main_floor: Annotated[Union[bool, None], Field(description='')] = None,
              has_rv_parking: Annotated[Union[bool, None], Field(description='')] = None,
              has_green_home: Annotated[Union[bool, None], Field(description='')] = None,
              has_accessible_home: Annotated[Union[bool, None], Field(description='')] = None,
              keyword_search: Annotated[Union[str, None], Field(description='')] = None,
              listing_type: Annotated[Union[str, None], Field(description='Multiple values can be entered and comma-separated Ex: ByAgent,ByOwner ByAgent: By agent ByOwner: By owner (FSBO) NewConstruction: New construction Foreclosures: Foreclosures')] = None) -> dict: 
    '''Search v2'''
    url = 'https://redfin-com-data.p.rapidapi.com/property/search-v2'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'locationId': locationId,
        'page': page,
        'search_by': search_by,
        'sort': sort,
        'search_type': search_type,
        'sold_within': sold_within,
        'min_price': min_price,
        'max_price': max_price,
        'home_type': home_type,
        'min_bedroom': min_bedroom,
        'max_bedroom': max_bedroom,
        'min_bathroom': min_bathroom,
        'status': status,
        'time_on_redfin': time_on_redfin,
        'min_square_feet': min_square_feet,
        'max_square_feet': max_square_feet,
        'min_lot_size': min_lot_size,
        'max_lot_size': max_lot_size,
        'min_stories': min_stories,
        'max_stories': max_stories,
        'min_year_built': min_year_built,
        'max_year_built': max_year_built,
        'has_exclude_55_communities': has_exclude_55_communities,
        'garage_spots': garage_spots,
        'pool_type': pool_type,
        'has_include_outdoor_parking': has_include_outdoor_parking,
        'has_air_conditioning': has_air_conditioning,
        'has_waterfront': has_waterfront,
        'has_view': has_view,
        'has_fireplace': has_fireplace,
        'has_fixer_upper': has_fixer_upper,
        'has_guest_house': has_guest_house,
        'has_elevator': has_elevator,
        'has_basement': has_basement,
        'has_washer_dryer_hookup': has_washer_dryer_hookup,
        'has_pets_allowed': has_pets_allowed,
        'has_primary_bedroom_on_main_floor': has_primary_bedroom_on_main_floor,
        'has_rv_parking': has_rv_parking,
        'has_green_home': has_green_home,
        'has_accessible_home': has_accessible_home,
        'keyword_search': keyword_search,
        'listing_type': listing_type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_by_url(url: Annotated[str, Field(description='')]) -> dict: 
    '''Search by URL'''
    url = 'https://redfin-com-data.p.rapidapi.com/property/search-url'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def property_details(url: Annotated[str, Field(description='1. The value of the url in the /Search endpoint Ex: /NY/Jamaica/9452-199th-St-11423/home/20743109 2. Or copy the URL from the browser Ex: https://www.redfin.com/NY/Jamaica/9452-199th-St-11423/home/20743109')]) -> dict: 
    '''Property details'''
    url = 'https://redfin-com-data.p.rapidapi.com/property/detail'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def property_detail_sphotos(url: Annotated[str, Field(description='1. The value of the url in the /Search endpoint Ex: /NY/Jamaica/9452-199th-St-11423/home/20743109 2. Or copy the URL from the browser Ex: https://www.redfin.com/NY/Jamaica/9452-199th-St-11423/home/20743109')]) -> dict: 
    '''Get photo of property detail'''
    url = 'https://redfin-com-data.p.rapidapi.com/property/detail-photos'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def agents_auto_complete(location: Annotated[str, Field(description='')]) -> dict: 
    '''agents/auto-complete'''
    url = 'https://redfin-com-data.p.rapidapi.com/agents/auto-complete'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def agents_search(location: Annotated[str, Field(description='location can be retrieved from /agents/auto-complete (data->name)')],
                  sub_location: Annotated[Union[str, None], Field(description='sub_location can be retrieved from /agents/auto-complete (data->subName)')] = None) -> dict: 
    '''agents/search'''
    url = 'https://redfin-com-data.p.rapidapi.com/agents/search'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
        'sub_location': sub_location,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def agents_detail(profile_url: Annotated[str, Field(description='profileUrl from agents/search endpoint')]) -> dict: 
    '''agents/detail'''
    url = 'https://redfin-com-data.p.rapidapi.com/agents/detail'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'profile_url': profile_url,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
async def get_full_redfin_sale_list(
    regionId: Annotated[str, Field(description="Redfin region ID, can be obtained via /properties/auto-complete")],
    limit: Annotated[Union[int, float, None], Field(description='Items per page, default 35')] = None,
    prices: Annotated[Union[str, None], Field(description='Price range')] = None,
    beds: Annotated[Union[int, float, None], Field(description='Number of bedrooms')] = None,
    baths: Annotated[Union[int, float, None], Field(description='Number of bathrooms')] = None,
    homeType: Annotated[Union[str, None], Field(description='Home type')] = None,
    squareFeet: Annotated[Union[str, None], Field(description='Square footage range')] = None,
    lotSize: Annotated[Union[str, None], Field(description='Lot size range')] = None,
    status: Annotated[Union[int, float, None], Field(description='Status')] = None,
    timeOnRedfin: Annotated[Union[str, None], Field(description='Time on Redfin')] = None,
    stories: Annotated[Union[str, None], Field(description='Number of stories')] = None,
    yearBuilt: Annotated[Union[str, None], Field(description='Year built')] = None,
    booleanFilters: Annotated[Union[str, None], Field(description='Boolean filters')] = None,
    pool: Annotated[Union[int, float, None], Field(description='Pool')] = None,
    garageSpots: Annotated[Union[int, float, None], Field(description='Garage spots')] = None,
    hoaFees: Annotated[Union[int, float, None], Field(description='HOA fees')] = None,
    priceSqft: Annotated[Union[str, None], Field(description='Price per sqft range')] = None,
    propertyTaxes: Annotated[Union[int, float, None], Field(description='Property taxes')] = None,
    acceptedFinancing: Annotated[Union[int, float, None], Field(description='Accepted financing')] = None,
    priceReduced: Annotated[Union[str, None], Field(description='Price reduced time')] = None,
    listingType: Annotated[Union[str, None], Field(description='Listing type')] = None,
    greatSchoolsRating: Annotated[Union[int, float, None], Field(description='GreatSchools rating')] = None,
    schoolTypes: Annotated[Union[str, None], Field(description='School types')] = None,
    walkScore: Annotated[Union[int, float, None], Field(description='Walk score')] = None,
    transitScore: Annotated[Union[int, float, None], Field(description='Transit score')] = None,
    bikeScore: Annotated[Union[int, float, None], Field(description='Bike score')] = None,
    openHouse: Annotated[Union[int, float, None], Field(description='Open house')] = None,
    keyword: Annotated[Union[str, None], Field(description='Keyword')] = None,
) -> dict:
    """Fetch up to 210 Redfin sale listings for the given search by fetching the first 6 pages in parallel (page size is 35)."""
    url = 'https://redfin-com-data.p.rapidapi.com/properties/search-sale'
    headers = {'x-rapidapi-host': 'redfin-com-data.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}

    import httpx, asyncio
    logged_pages = set()
    async def fetch_page(page):
        params = {
            'regionId': regionId,
            'limit': limit if limit is not None else 35,
            'page': page,
            'prices': prices,
            'beds': beds,
            'baths': baths,
            'homeType': homeType,
            'squareFeet': squareFeet,
            'lotSize': lotSize,
            'status': status,
            'timeOnRedfin': timeOnRedfin,
            'stories': stories,
            'yearBuilt': yearBuilt,
            'booleanFilters': booleanFilters,
            'pool': pool,
            'garageSpots': garageSpots,
            'hoaFees': hoaFees,
            'priceSqft': priceSqft,
            'propertyTaxes': propertyTaxes,
            'acceptedFinancing': acceptedFinancing,
            'priceReduced': priceReduced,
            'listingType': listingType,
            'greatSchoolsRating': greatSchoolsRating,
            'schoolTypes': schoolTypes,
            'walkScore': walkScore,
            'transitScore': transitScore,
            'bikeScore': bikeScore,
            'openHouse': openHouse,
            'keyword': keyword,
        }
        params = {k: v for k, v in params.items() if v is not None}
        logger.info(f"Requesting page {page} with params: {params}")
        async with httpx.AsyncClient() as client:
            resp = await client.get(url, headers=headers, params=params)
            result = resp.json()
        if page not in logged_pages:
            if isinstance(result, dict):
                data = result.get('data', {})
                if isinstance(data, list):
                    logger.info(f"Page {page} returned {len(data)} items.")
                elif isinstance(data, dict):
                    homes = data.get('homeData', [])
                    logger.info(f"Page {page} returned {len(homes)} items.")
                else:
                    logger.info(f"Page {page} returned data of unknown type.")
            else:
                logger.info(f"Page {page} returned non-dict result.")
            logged_pages.add(page)
        return result

    async def gather_first_6_pages():
        # Fetch pages 1-6 in parallel
        tasks = [fetch_page(page) for page in range(1, 7)]
        results = await asyncio.gather(*tasks)
        all_results = []
        for result in results:
            if isinstance(result, dict):
                data = result.get('data', {})
                if isinstance(data, list):
                    all_results.extend(data)
                elif isinstance(data, dict):
                    homes = data.get('homeData', [])
                    if isinstance(homes, list):
                        all_results.extend(homes)
            elif isinstance(result, list):
                all_results.extend(result)
        return {'all_results': all_results[:210]}

    return await gather_first_6_pages()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
