import pandas as pd
from hdbcli import dbapi
from taskweaver.plugin import Plugin, register_plugin

@register_plugin
class HanaConnect(Plugin):
    def __call__(self, query: str):
        # Connect to SAP HANA database using credentials from the plugin configuration
        conn = dbapi.connect(
            address=self.config.get("hana_host"),
            port=int(self.config.get("hana_port")),
            user=self.config.get("hana_user"),
            password=self.config.get("hana_password")
        )

        try:
            # Create a cursor object and execute the SQL query
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            df = pd.DataFrame(result, columns=columns)

            # Prepare and return a description of the result
            description = "No data returned for query." if df.empty else f"Data returned for query with {len(df)} rows."
            return df, description
        except Exception as e:
            return pd.DataFrame(), f"Error executing query: {e}"
        finally:
            # Ensure cursor and connection are closed
            if cursor:
                cursor.close()
            if conn:
                conn.close()

# Example usage of the plugin
if __name__ == "__main__":
    config = {
        "hana_host": "your_hana_host",
        "hana_port": "your_hana_port",
        "hana_user": "your_hana_username",
        "hana_password": "your_hana_password"
    }

    hana_plugin = HanaConnect(config)
    query = "SELECT * FROM ZDEMO_SOI"  # Replace with your required SAP custom table
    hana_data, hana_description = hana_plugin(query)

    print(hana_description)
    print(hana_data)
