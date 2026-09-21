from app import create_app

# Cria a instância do Flask configurada
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)