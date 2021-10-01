
---
title: 'Next Terminal v1.1.0 发布，HTML5 的远程桌面网关'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6870'
author: 开源中国
comments: false
date: Thu, 30 Sep 2021 19:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6870'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Next Terminal v1.1.0 已经发布，HTML5 的远程桌面网关。</p> 
<h2>更新内容</h2> 
<ul> 
 <li>增加sshd服务功能，支持通过ssh协议访问资产，支持TOTP验证，支持实时监控和录屏</li> 
 <li>原生ssh增加监控功能</li> 
 <li>接入网关增加手动重连功能</li> 
 <li>优化资产授权逻辑</li> 
</ul> 
<h2>如何升级？</h2> 
<h3>docker</h3> 
<p>以sqlite模式为例，修改 docker-compose.yml，增加标记 <strong>#增加</strong> 下面的内容</p> 
<pre><code>version: '3.3'
services:
  guacd:
    image: dushixiang/guacd:1.3.0
    volumes:
      - ./data:/usr/local/next-terminal/data
    restart:
          always
  next-terminal:
    image: dushixiang/next-terminal:latest
    environment:
      DB: sqlite
      GUACD_HOSTNAME: guacd
      GUACD_PORT: 4822
      # 增加
      SSHD_ENABLE: "true"
    ports:
      - "8088:8088"
      # 增加
      - "8089:8089"
    volumes:
      - /etc/machine-id:/etc/machine-id
      - /etc/localtime:/etc/localtime
      - ./data:/usr/local/next-terminal/data
      # 增加
      - ~/.ssh/id_rsa:/root/.ssh/id_rsa
    restart:
          always
</code></pre> 
<h3>原生</h3> 
<p>修改 config.yml 增加最下方的 sshd 配置</p> 
<pre><code>db: sqlite
# 当db为sqlite时mysql的配置无效
#mysql:
#  hostname: 172.16.101.32
#  port: 3306
#  username: root
#  password: mysql
#  database: next-terminal

# 当db为mysql时sqlite的配置无效
sqlite:
  file: 'next-terminal.db'
server:
  addr: 0.0.0.0:8088
# 当设置下面两个参数时会自动开启https模式(前提是证书文件存在)
#  cert: /root/next-terminal/cert.pem
#  key: /root/next-terminal/key.pem

# 授权凭证和资产的密码，密钥等敏感信息加密的key，默认`next-terminal`
#encryption-key: next-terminal
guacd:
  hostname: 127.0.0.1
  port: 4822
  # 此路径需要为绝对路径，并且next-terminal和guacd都能访问到
  recording: '/usr/local/next-terminal/data/recording'
  # 此路径需要为绝对路径，并且next-terminal和guacd都能访问到
  drive: '/usr/local/next-terminal/data/drive'

# 增加以下内容
sshd:
  # 是否开启sshd服务
  enable: true
  # sshd 监听地址
  addr: 0.0.0.0:8089
  # sshd 使用的私钥地址
  key: ~/.ssh/id_rsa
</code></pre> 
<p>详情查看：<a href="https://gitee.com/dushixiang/next-terminal/releases/v1.1.0">https://gitee.com/dushixiang/next-terminal/releases/v1.1.0</a></p>
                                        </div>
                                      
</div>
            