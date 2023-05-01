output "region"{
    value = var.region
    description = "Google Cloud Region"
}

output "project_id"{
    value = var.project_id
    description = "Google Cloud Project ID"
}

output "zone"{
    value = var.zone
    description = "Google Cloud Region"
}

output "ml_bucket"{
    value = google_storage_bucket.ml-storage.name
    description = "Google Cloud Storage Bucket for storing ml model"
}