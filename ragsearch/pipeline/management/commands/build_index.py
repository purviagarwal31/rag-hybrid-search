from django.core.management.base import BaseCommand
from pipeline.data_loader import load_dataset
from pipeline.embedder import generate_embeddings, build_faiss_index, save_index

class Command(BaseCommand):
    help = 'Builds the FAISS index from the dataset'

    def handle(self, *args, **kwargs):
        df = load_dataset()
        if df.empty:
            self.stdout.write(self.style.ERROR("❌ Dataset could not be loaded."))
            return

        embeddings = generate_embeddings(df)
        index = build_faiss_index(embeddings)
        save_index(index, df)

        self.stdout.write(self.style.SUCCESS("✅ FAISS index and metadata saved successfully."))
