terraform {
  required_providers {
    mgc = {
      source = "magalucloud/mgc"
    }

  }
}

#resource "mgc_ssh_keys" "key" {
#  name = "codafofo"
#  key = "ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAG9H2+dybiy3UPHxVZtnguMCtQZsBnKPkLS65wpQ7cIzticsh9FJAO8Hv2FSmsFhU/bXOfXieu6/D7VD87pgvY= brenopelegrin@lenovo"
#}

# Create a VM at Sudeste br-se1
resource "mgc_virtual_machine_instances" "boituvinhatest" {
  provider = mgc.sudeste
  name     = "boituvinhatest"
  machine_type = {
    name = "BV4-8-100"
  }
  image = {
    name = "cloud-ubuntu-22.04 LTS"
  }
  network = {
    associate_public_ip = true
    delete_public_ip    = false
    interface = {
      security_groups = [{
        id = "576d3982-506c-4ad9-b12c-5fbec5ba7922"
      }]
    }
  }
  ssh_key_name = "codafofo"

  connection {
    type     = "ssh"
    user     = "ubuntu"
    private_key = file("~/.ssh/id_magalu")
    host     = self.network.public_address
  }

  provisioner "remote-exec" {
    inline = [
      "sudo snap install docker",
      "git clone https://github.com/brenopelegrin/pytasks.git -b magalu-deploy",
      "export JWT_PRIVATE_PEM=$(cat pytasks/examples/keys/jwtRS256.key)",
      "export JWT_PUBLIC_PEM=$(cat pytasks/examples/keys/jwtRS256.key.pub)",
      "cd pytasks && docker compose up -d"
    ]
  }
}