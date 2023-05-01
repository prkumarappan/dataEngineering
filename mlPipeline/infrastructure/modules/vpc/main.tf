# VPC
resource "google_compute_network" "vpc" {
  name = local.vpc_NM
  auto_create_subnetworks = "false"
}

#subnet 
resource "google_compute_subnetwork" "subnet" {
  name = local.subnet_NM
  region = var.region
  network = google_compute_network.vpc.name
  ip_cidr_range = "10.10.0.0/24"
  }