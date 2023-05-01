# Source: root 
# modules included: vpc and gke
# Goal: Create a GKE cluster in a VPC

module "vpc" {
    source = "../modules/vpc"
    project_id = var.project_id
    region = var.region
    zone = var.zone
}

module "gke"{
    source = "../modules/gke"
    project_id = var.project_id
    region = var.region
    zone = var.zone
    network = module.vpc.vpc
    subnetwork = module.vpc.subnet
}
