provider "google" {
    project = var.project_id
    region = var.region
    zone = var.zone
    credentials = "${file(var.credentials_file)}"
}

resource "random_string" "randomString" {
    length = 16
    special = false
    upper = false
}