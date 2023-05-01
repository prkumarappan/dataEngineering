terraform {
  required_version = ">=1.4.4"
    required_providers {
        google = {
        source = "hashicorp/google"
        version = ">=4.63.1"
        }
        random = {
        source = "hashicorp/random"
        version = ">=3.5.1"
        }
    }
}