variable "project_id"{
    description = "value of project_id"
    type = string
}

variable "region"{
    description = "value of region"
    type = string
}

variable "zone"{
    description = "value of zone"
    type = string
}

variable "network"{
    description = "value of vpc"
}

variable "subnetwork"{
    description = "value of subnet"
}

variable "gke_username"{
    description = "value of gke_username"
    type = string
    default = "admin"
}

variable "gke_password"{
    description = "value of gke_password"
    type = string
    default = "admin"
}

variable "gke_num_nodes"{
    description = "value of gke_num_nodes"
    type = number
    default = 1
}