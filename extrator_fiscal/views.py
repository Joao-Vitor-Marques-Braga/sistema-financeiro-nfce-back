# apps/extrator_fiscal/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import ExtratorFiscalService

class ExtratorFiscalAPIView(APIView):
    """
    API View para receber um arquivo PDF de nota fiscal e extrair os dados.
    """
    def post(self, request, *args, **kwargs):
        # 1. Pega o arquivo da requisição (o frontend deve enviar com a chave 'pdf_file')
        pdf_file = request.FILES.get('pdf_file')

        if not pdf_file:
            return Response(
                {"error": "Nenhum arquivo PDF foi enviado."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # 2. Instancia e chama o serviço que contém a lógica de negócio
            extrator_service = ExtratorFiscalService()
            dados_extraidos = extrator_service.extrair_dados_do_pdf(pdf_file)

            # 3. Retorna os dados extraídos com sucesso
            return Response(dados_extraidos, status=status.HTTP_200_OK)

        except Exception as e:
            # Em caso de qualquer erro no processo, retorna uma resposta genérica
            return Response(
                {"error": f"Ocorreu um erro ao processar o arquivo: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )