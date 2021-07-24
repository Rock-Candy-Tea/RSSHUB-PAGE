
---
title: 'Masterlab-docker 1.4.1 发布，基于 Docker 方式部署 Masterlab'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1801'
author: 开源中国
comments: false
date: Fri, 23 Jul 2021 15:29:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1801'
---

<div>   
<div class="content">
                                                                                            <p>此项目是以Docker方式部署项目管理工具：Masterlab。<br> Masterlab的运行依赖于 Mysql Nginx|Apache PHP环境，Docker方式可以很快速的进行跨平台部署 。  <br> 相关镜像已经部署到DockerHub上。</p> 
<div> 
 <pre><code># 镜像仓库
https://hub.docker.com/repository/docker/gopeak/masterlab
# FPM和Cli镜像，主要是编译和加载了swoole,redis扩展
gopeak/masterlab:php-fpm-74
gopeak/masterlab:php-cli-74

</code></pre> 
</div> 
<p>提供 Docker Run 和 Docker-compose 两种部署方式。</p> 
<p>Docker Run方式： <a href="https://gitee.com/firego/masterlab-docker/blob/master/STEP.md">https://gitee.com/firego/masterlab-docker/blob/master/STEP.md</a>   </p> 
<p>Docker-compose方式： <a href="https://gitee.com/firego/masterlab-docker/blob/master/README.md">https://gitee.com/firego/masterlab-docker/blob/master/README.md</a>  </p>
                                        </div>
                                      
</div>
            