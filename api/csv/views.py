
from rest_framework.views import APIView
from utils.csv_utils import ImportCSV
import io

class ImportView(APIView):
    def post(self, request):
        try:
            csv_file = request.FILES['file']
            # if not csv_file.name.endswith('.csv'):
            #     return Response({'status':'error','message':'invalid file format'})
            
            csv = ImportCSV().read_excel_file(csv_file)
            print(csv)
            return Response({'status':'success','data':csv})
        except Exception as e:
            print(e)
            raise e