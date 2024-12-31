import os
import asyncio
from metaapi_cloud_sdk import MetaApi
from datetime import datetime

token = os.getenv('TOKEN') or 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NjVlMDI2MGQ2NDVlY2QxODQyOWJiM2VhZmRiNzlhMyIsInBlcm1pc3Npb25zIjpbXSwiYWNjZXNzUnVsZXMiOlt7ImlkIjoidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpIiwibWV0aG9kcyI6WyJ0cmFkaW5nLWFjY291bnQtbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6ZGY2N2Y1YzAtNDQ3Yy00Y2I0LWEzYTYtOWRmMTc5YzRhNDBlIl19LHsiaWQiOiJtZXRhYXBpLXJlc3QtYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDpkZjY3ZjVjMC00NDdjLTRjYjQtYTNhNi05ZGYxNzljNGE0MGUiXX0seyJpZCI6Im1ldGFhcGktcnBjLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbImFjY291bnQ6JFVTRVJfSUQkOmRmNjdmNWMwLTQ0N2MtNGNiNC1hM2E2LTlkZjE3OWM0YTQwZSJdfSx7ImlkIjoibWV0YWFwaS1yZWFsLXRpbWUtc3RyZWFtaW5nLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbImFjY291bnQ6JFVTRVJfSUQkOmRmNjdmNWMwLTQ0N2MtNGNiNC1hM2E2LTlkZjE3OWM0YTQwZSJdfSx7ImlkIjoibWV0YXN0YXRzLWFwaSIsIm1ldGhvZHMiOlsibWV0YXN0YXRzLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDpkZjY3ZjVjMC00NDdjLTRjYjQtYTNhNi05ZGYxNzljNGE0MGUiXX0seyJpZCI6InJpc2stbWFuYWdlbWVudC1hcGkiLCJtZXRob2RzIjpbInJpc2stbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6ZGY2N2Y1YzAtNDQ3Yy00Y2I0LWEzYTYtOWRmMTc5YzRhNDBlIl19LHsiaWQiOiJtZXRhYXBpLXJlYWwtdGltZS1zdHJlYW1pbmctYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTp3czpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6ZGY2N2Y1YzAtNDQ3Yy00Y2I0LWEzYTYtOWRmMTc5YzRhNDBlIl19LHsiaWQiOiJjb3B5ZmFjdG9yeS1hcGkiLCJtZXRob2RzIjpbImNvcHlmYWN0b3J5LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDpkZjY3ZjVjMC00NDdjLTRjYjQtYTNhNi05ZGYxNzljNGE0MGUiXX1dLCJpZ25vcmVSYXRlTGltaXRzIjpmYWxzZSwidG9rZW5JZCI6IjIwMjEwMjEzIiwiaW1wZXJzb25hdGVkIjpmYWxzZSwicmVhbFVzZXJJZCI6IjY2NWUwMjYwZDY0NWVjZDE4NDI5YmIzZWFmZGI3OWEzIiwiaWF0IjoxNzM1NTc1NTkwLCJleHAiOjE3MzgxNjc1OTB9.XFEBxWGA-TKRXxpPmCwAsVd2iqz6lhmILt6X0KTECcVziRoS8CORzn1_hwpXQTMUmd2Dlt8kSCBR2xqz7NbFvvjHG7inKljxzjlRYhXN0w7bXe77rSb-IdashQMV3SlCFj0H-qOcSD1-7SbZwPhWRA0jiooiGFjpsFLjKSl6AfYWL2OVVWfgZ8x7CXtii2zEz31K5lVay7HsR7YEch0dD80fjJ4t4H1fwSaMSSP0fBqU_kt3wnpfGQjFExtAqqX3A83WLn8wIPQLY-Mrbr7_5lJ8lGpEXeM1LUytMtd0wUGsk2VYS2YuhzqMEX8pb4A-C2f12BxHq_KnrDgqOPeXkq881fOkWnuldrAaDVDF0n8LhN5teINS8IjTWvFcYB9sa2kQI8baarAVUexLPrtG7fwG6zbOftYlprpeRZTAtS2cEpDb6rOsZHtuv9HX8XtyqQCo73brEMNfhBIprpXCZXKPv7IeYDebHmJiSxaNo2WAofj8VcnuarUAEZMe0Wc8xcZslwBFbuf4ub6FTku1HSZFDqmQfMqPR9wRG4Tma6_X_0nTkt2Lk36xeRyVyialx3o4cuYkMAKk_CoU_LCRIqfm0d3Y_xhl8oY0f8zW8s5XC3P7aFVqqwixFp_f2_ify1rbw7nCKbZ2VqELe_-QXWUiLGnKwjcXym3Be_ZXaDw'
accountId = os.getenv('ACCOUNT_ID') or 'df67f5c0-447c-4cb4-a3a6-9df179c4a40e'

async def test_meta_api_synchronization():
    api = MetaApi(token)
    try:
        account = await api.metatrader_account_api.get_account(accountId)
        initial_state = account.state
        deployed_states = ['DEPLOYING', 'DEPLOYED']

        if initial_state not in deployed_states:
            #  wait until account is deployed and connected to broker
            print('Deploying account')
            await account.deploy()

        print('Waiting for API server to connect to broker (may take couple of minutes)')
        await account.wait_connected()

        # connect to MetaApi API
        connection = account.get_streaming_connection()
        await connection.connect()
        
        # trade
        print('Submitting pending order')
        try:
            result = await connection.create_limit_buy_order(
                'GBPUSD', 0.07, 1.0, 0.9, 2.0, {'comment': 'comm', 'clientId': 'TE_GBPUSD_7hyINWqAlE'}
            )
            print('Trade successful, result code is ' + result['stringCode'])
        except Exception as err:
            print('Trade failed with error:')
            print(api.format_error(err))

        if initial_state not in deployed_states:
            # undeploy account if it was undeployed
            print('Undeploying account')
            await connection.close()
            await account.undeploy()

    except Exception as err:
        print(api.format_error(err))
    exit()


asyncio.run(test_meta_api_synchronization())
