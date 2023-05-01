# enable cloud resource manager
resource "google_project_service" "cloud_resource_manager" {
  service = "cloudresourcemanager.googleapis.com"
  disable_dependent_services = true
}

# enable compute engine 
resource "google_project_service" "compute_engine" {
  service = "compute.googleapis.com"
  disable_dependent_services = true
}

#enable kubernetes engine
resource "google_project_service" "kubernetes_engine" {
  service = "container.googleapis.com"
  disable_dependent_services = true
}

# sleep for 2 minutes to allow APIs to enable
resource "time_sleep" "google_cloud_api_enabling" {
  depends_on = [
    google_project_service.cloud_resource_manager,
    google_project_service.compute_engine,
    google_project_service.kubernetes_engine
  ]
  create_duration = "2m"
}

# google storage bucket for storing ml model
resource "google_storage_bucket" "ml-storage" {
    name = "ml-storage-${var.project_id}"
    location = var.location
    force_destroy = true
    uniform_bucket_level_access = true
    versioning {
        enabled = true
    }
}

resource "null_resource" "upload_folder" {
  triggers = {
    folder_path = var.ml_model_path
  }

  provisioner "local-exec" {
    command = <<EOF
      gsutil cp -r ${null_resource.upload_folder.triggers.folder_path}/* gs://${google_storage_bucket.ml-storage.name}
    EOF
  }
  
}