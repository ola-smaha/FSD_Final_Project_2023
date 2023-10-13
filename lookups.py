from enum import Enum

class Errors(Enum):
    DB_RETURN_QUERY_ERROR = "DB Return Query Error"
    NO_ERROR = "No Errors"
    EXECUTE_QUERY_ERROR = "Error executing the query"
    RETURN_DF_CSV_ERROR = "Error returning dataframe from CSV"
    RETURN_DF_SQL_ERROR = "Error returning dataframe from SQL"
    UNDEFINED_ERROR = "Undefined Error"
    ERROR_CONNECTING_TO_DB = "Error connecting to database"
    ERROR_CLOSING_CONN = "Error closing connection, check if session exists"
    ERROR_UNDEFINED_SOURCE = "This source is not a defined source in our datasets"
    PREHOOK_SQL_ERROR = "Prehook error"

class TransformationErrors(Enum):
    FETCHING_DATA_FROM_SOURCE = "Error fetching data from source"
    ERROR_STATUS_CODE = "Error: Received status code"
    READ_DATA_FN_ERROR = "Error processing results"
    CLEAN_DALLAS_DF_ERROR = "Error doing pandas transformations on Dallas datasets"
    CLEAN_BLOOMINGTON_DF_ERROR = "Error doing pandas transformations on Bloomington dataset"
    CLEAN_NORFOLK_DF_ERROR = "Error doing pandas transformations on Norfolk dataset"
    CLEAN_AUSTIN_DF_ERROR = "Error doing pandas transformations on Austin dataset"
    CLEAN_SONOMA_DF_ERROR = "Error doing pandas transformations on Sonoma dataset"
    CLEAN_ALL_DATA = "Error in: clean_all_data"

class DataSources(Enum):
    SHELTER_SONOMA = "https://data.sonomacounty.ca.gov/resource/924a-vesw.json?$select=id,type,breed,color,sex,date_of_birth,intake_date,outcome_date,intake_type,outcome_type"
    SHELTER_AUSTIN_INTAKES = "https://data.austintexas.gov/resource/wter-evkm.json?$select=animal_id,animal_type,breed,color,datetime,intake_type"
    SHELTER_AUSTIN_OUTCOMES = "https://data.austintexas.gov/resource/9t4d-g238.json?$select=animal_id,sex_upon_outcome,date_of_birth,datetime,outcome_type"
    SHELTER_NORFOLK = "https://data.norfolk.gov/resource/vfm4-5wv6.json?$select=animal_id,animal_type,primary_breed,primary_color,sex,years_old,months_old,intake_date,outcome_date,intake_type,outcome_type"
    SHELTER_BLOOMINGTON = "https://data.bloomington.in.gov/resource/e245-r9ub.json?$select=id,speciesname,breedname,basecolour,sexname,animalage,intakedate,movementdate,intakereason,movementtype"
    SHELTER_DALLAS_2017_2018 = "https://www.dallasopendata.com/resource/wb7n-sdxi.json?$select=animal_id,animal_type,animal_breed,intake_date,intake_time,outcome_date,outcome_time,intake_type,outcome_type"
    SHELTER_DALLAS_2018_2019 = "https://www.dallasopendata.com/resource/kf5k-aswg.json?$select=animal_id,animal_type,animal_breed,intake_date,intake_time,outcome_date,outcome_time,intake_type,outcome_type"
    SHELTER_DALLAS_2019_2020 = "https://www.dallasopendata.com/resource/7h2m-3um5.json?$select=animal_id,animal_type,animal_breed,intake_date,intake_time,outcome_date,outcome_time,intake_type,outcome_type"
    SHELTER_DALLAS_2020_2021 = "https://www.dallasopendata.com/resource/sq59-vp2t.json?$select=animal_id,animal_type,animal_breed,intake_date,intake_time,outcome_date,outcome_time,intake_type,outcome_type"
    SHELTER_DALLAS_2021_2022 = "https://www.dallasopendata.com/resource/uu3b-ppfz.json?$select=animal_id,animal_type,animal_breed,intake_date,intake_time,outcome_date,outcome_time,intake_type,outcome_type"
    SHELTER_DALLAS_2022_2023 = "https://www.dallasopendata.com/resource/f77p-sgrc.json?$select=animal_id,animal_type,animal_breed,intake_date,intake_time,outcome_date,outcome_time,intake_type,outcome_type"
    
    # Income CSV download button links (using inspect)
    PER_CAPITA_SONOMA_INCOME = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1138&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=PCPI06097&scale=left&cosd=2009-01-01&coed=2021-01-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Annual&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-10-12&revision_date=2023-10-12&nd=1969-01-01"
    PER_CAPITA_AUSTIN_INCOME = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1138&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=PCPI48015&scale=left&cosd=2009-01-01&coed=2021-01-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Annual&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-10-12&revision_date=2023-10-12&nd=1969-01-01"
    PER_CAPITA_NORFOLK_INCOME = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1138&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=PCPI51710&scale=left&cosd=2009-01-01&coed=2021-01-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Annual&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-10-12&revision_date=2023-10-12&nd=1969-01-01"
    PER_CAPITA_BLOOMINGTON_MONROE_INCOME = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1138&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=PCPI18105&scale=left&cosd=2009-01-01&coed=2021-01-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Annual&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-10-12&revision_date=2023-10-12&nd=1969-01-01"
        # Note: Norfolk city does not belong to a county, Bloomington is in Monroe county, link is for Monroe per capita income
    PER_CAPITA_DALLAS_INCOME = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1138&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=PCPI48113&scale=left&cosd=2009-01-01&coed=2021-01-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Annual&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-10-12&revision_date=2023-10-12&nd=1969-01-01"
    
    # Population CSV download button links (using inspect)
    POPULATION_SONOMA = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1138&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=CASONO6POP&scale=left&cosd=2009-01-01&coed=2022-01-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Annual&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-10-11&revision_date=2023-10-11&nd=1970-01-01"
    POPULATION_AUSTIN = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1138&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=TXAUST5POP&scale=left&cosd=2009-01-01&coed=2022-01-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Annual&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-10-11&revision_date=2023-10-11&nd=1970-01-01"
    POPULATION_NORFOLK_CITY = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1138&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=VANORF5POP&scale=left&cosd=2009-01-01&coed=2022-01-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Annual&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-10-11&revision_date=2023-10-11&nd=1970-01-01"
    POPULATION_BLOOMINGTON_MONROE = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1318&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=INMONR5POP&scale=left&cosd=2009-01-01&coed=2022-01-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Annual&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-10-12&revision_date=2023-10-12&nd=1970-01-01"
    POPULATION_DALLAS = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1138&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=TXDALL3POP&scale=left&cosd=2009-01-01&coed=2022-01-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Annual&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-10-11&revision_date=2023-10-11&nd=1970-01-01"
    
    # Unemployment CSV download button links (using inspect)
    UNEMPLOYMENT_RATE_SONOMA = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1318&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=LAUCN060970000000003A&scale=left&cosd=2009-01-01&coed=2022-01-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Annual&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-10-11&revision_date=2023-10-11&nd=1990-01-01"
    UNEMPLOYMENT_RATE_AUSTIN = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1138&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=TXAUST5URN&scale=left&cosd=2009-01-01&coed=2023-08-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-10-11&revision_date=2023-10-11&nd=1990-01-01"
    UNEMPLOYMENT_RATE_NORFOLK_CITY = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1138&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=VANORF5URN&scale=left&cosd=2009-01-01&coed=2023-08-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-10-11&revision_date=2023-10-11&nd=1990-01-01"
    UNEMPLOYMENT_RATE_BLOOMINGTON = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1138&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=BLOO018URN&scale=left&cosd=2009-01-01&coed=2023-08-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-10-11&revision_date=2023-10-11&nd=1990-01-01"
    UNEMPLOYMENT_RATE_DALLAS = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1138&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=TXDALL3URN&scale=left&cosd=2009-01-01&coed=2023-08-01&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2023-10-11&revision_date=2023-10-11&nd=1990-01-01"

class StagingTablesNames(Enum):
    SONOMA_INTAKES_OUTCOMES = "intakes_outcomes_sonoma"
    AUSTIN_INTAKES_OUTCOMES = "intakes_outcomes_austin"
    NORFOLK_INTAKES_OUTCOMES = "intakes_outcomes_norfolk"
    BLOOMINGTON_INTAKES_OUTCOMES = "intakes_outcomes_bloomington"
    DALLAS_INTAKES_OUTCOMES = "intakes_outcomes_dallas"
    PER_CAPITA_SONOMA_INCOME = "PER_CAPITA_SONOMA_INCOME"
    PER_CAPITA_AUSTIN_INCOME = "per_capita_austin_income"
    PER_CAPITA_NORFOLK_INCOME = "per_capita_norfolk_income"
    PER_CAPITA_BLOOMINGTON_INCOME = "per_capita_bloomington_income"
    PER_CAPITA_DALLAS_INCOME = "per_capita_dallas_income"
    POPULATION_SONOMA = "population_sonoma"
    POPULATION_AUSTIN = "population_austin"
    POPULATION_NORFOLK_CITY = "population_norfolk_city"
    POPULATION_BLOOMINGTON = "population_bloomington"
    POPULATION_DALLAS = "population_dallas"
    UNEMPLOYMENT_RATE_SONOMA = "unemployment_rate_sonoma"
    UNEMPLOYMENT_RATE_AUSTIN = "unemployment_rate_austin"
    UNEMPLOYMENT_RATE_NORFOLK_CITY = "unemployment_rate_norfolk_city"
    UNEMPLOYMENT_RATE_BLOOMINGTON = "unemployment_rate_bloomington"
    UNEMPLOYMENT_RATE_DALLAS = "unemployment_rate_dallas"

class InputTypes(Enum):
    CSV = "csv"
    SQL = "sql"
    TXT = "txt"

class DestinationSchemaName(Enum):
    Datawarehouse = 'dw_reporting_schema'

class PreHookSteps(Enum):
    EXECUTE_SQL_QUERIES = "Error in execute_sql_folder_prehook"
    CREATE_SQL_STAGING = "Error in create_sql_staging_tables"
    CREATE_TABLE_IDX = "Error in create_sql_stg_table_idx"

class SQLCommandsPath(Enum):
    SQL_FOLDER = "./SQL_Files/"