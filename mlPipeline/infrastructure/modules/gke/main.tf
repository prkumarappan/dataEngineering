# GKE cluster
resource "google_container_cluster" "primary" {
  name = local.conrainer_cluster_NM
  location = var.zone
  remove_default_node_pool = true
  initial_node_count = 1

  network = var.network
  subnetwork = var.subnetwork
}

# Seperately managed nood pool
resource "google_container_node_pool" "primary_nodes" {
  name = google_container_cluster.primary.name
  location = google_container_cluster.primary.location
  cluster = google_container_cluster.primary.name
  node_count = var.gke_num_nodes

  node_config {
    oauth_scopes = [
      "https://www.googleapis.com/auth/logging.write",
      "https://www.googleapis.com/auth/monitoring", 
      "https://www.googleapis.com/auth/cloud-platform",
      "https://www.googleapis.com/auth/devstorage.read_only"
    ]

    labels = {
      env = var.project_id
    }

    # High memory
    machine_type = "n1-highmem-8"
    tags = ["gke-node", google_container_cluster.primary.name]
    metadata = {
      disable-legacy-endpoints = "true"
    }
  }
}