output "vpc"{
    value = google_compute_network.vpc.name
    description = "Google Cloud VPC Name"
}

output "subnet" {
    value = google_compute_subnetwork.subnet.name
    description = "Google Cloud Subnet Name"
}