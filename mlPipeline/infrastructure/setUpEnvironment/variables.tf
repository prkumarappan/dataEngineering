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

variable "credentials_file" {
    description = "value of credentials_file"
    type = string
}

variable "service_account_name"{
    description = "value of service account name"
    type = string
}

variable "location"{
    description = "value of Cloud Storage bucket location"
    type = string
    default = "US"
}

variable "ml_model_path"{
    description = "value of ml model path"
    type = string
}