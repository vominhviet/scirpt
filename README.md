## Installation Guide
A CVAT installation guide for different operating systems.

- cài đặt docker 

```bash
sudo apt-get update
sudo apt-get --no-install-recommends install -y \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg-agent \
  software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) \
  stable"
sudo apt-get update
sudo apt-get --no-install-recommends install -y \
  docker-ce docker-ce-cli containerd.io docker-compose-plugin
```
- phần quyền cho docker
```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```
## Ubuntu 22.04/20.04 (x86_64/amd64)

- Clone Cvat 

```bash 
git clone https://github.com/cvat-ai/cvat
cd cvat
```
- export CVAT_HOST environment variable 

```bash
 export CVAT_HOST=<YOUR_DOMAIN>
```
- Run docker containers
```bash
docker compose up -d
```
- Tạo account cho cvat 
```bash
docker exec -it cvat_server bash -ic 'python3 ~/manage.py createsuperuser'
```
## Windows 10
- Install WSL2
- Install Docker desktop
- Install Git
- Clone Cvat 

```bash 
git clone https://github.com/cvat-ai/cvat
cd cvat
```
- export CVAT_HOST environment variable 

```bash
 export CVAT_HOST=<YOUR_DOMAIN>
```
- Run docker containers
```bash
docker compose up -d
```
- Tạo account cho cvat 
```bash
docker exec -it cvat_server bash -ic 'python3 ~/manage.py createsuperuser'
```