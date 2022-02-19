using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using System.Net;
using System.Text.Json;

namespace ConsoleTests
{
    internal class Program
    {
        private static void Main(string[] args)
        {
            // replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
            string base_url = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol="
            string apiKey = File.ReadAllText(key.txt);
            Uri queryUri = new Uri(base_url + symbol + "&apikey=" + apiKey);

            using (WebClient client = new WebClient())
            {
                // if using .NET Core (System.Text.Json)
                // using .NET Core libraries to parse JSON is more complicated. For an informative blog post
                // https://devblogs.microsoft.com/dotnet/try-the-new-system-text-json-apis/
		
                dynamic json_data = JsonSerializer.Deserialize<Dictionary<string, dynamic>>(client.DownloadString(queryUri));
		
                // -------------------------------------------------------------------------

                // do something with the json_data
            }
        }
    }
}