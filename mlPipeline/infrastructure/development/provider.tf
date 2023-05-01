# In this file we are defining the provider for our terraform project

provider "google" {
    project = var.project_id
    region = var.region
    zone = var.zone
    credentials = "${file(var.credentials_file)}"
}
