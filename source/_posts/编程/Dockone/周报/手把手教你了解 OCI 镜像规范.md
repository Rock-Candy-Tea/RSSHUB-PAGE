
---
title: '手把手教你了解 OCI 镜像规范'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=3953'
author: Dockone
comments: false
date: 2021-12-07 05:09:50
thumbnail: 'https://picsum.photos/400/300?random=3953'
---

<div>   
<br>在云原生应用的开发中，应用会被打包成容器镜像。容器镜像遵循 OCI 镜像规范。了解 OCI 镜像规范，对构建容器镜像有重要的作用。<br>
<br>在介绍 OCI 镜像规范之前，首先需要介绍内容可寻址的文件系统。<br>
<h3>内容可寻址的文件系统</h3>我们通常使用的文件系统是根据路径来查找文件的，比如 <code class="prettyprint">/etc/nginx/nginx.conf</code> 指向的就是文件系统上的一个文件。这种寻址方式很容易理解，使用起来也简单。其中的问题在于，对于同一个路径，它所指向的文件的内容是可变的。在不同的时间点上访问同一个路径的文件，它所包含的内容会产生变化。<br>
<br>容器镜像的一个重要优势是不可变。为了满足这种需求，容器镜像使用的是内容可寻址的方式。基本的思路是对每一个文件，使用摘要算法得到该文件的摘要。使用该摘要作为该文件的寻址方式。SHA-256 和 SHA-512 是常用的摘要算法。<br>
<br>当文件的内容发生变化时，它的摘要也会发生变化。使用同一个摘要，总是可以找到同样的内容。在这种寻址方式下，可以把文件系统看成是一个巨大的哈希表。哈希表的键是摘要，而对应的值则是文件的内容。<br>
<h3>工具支持</h3>在开始之前，需要安装 skopeo 和 jq 两个工具。以 Ubuntu 为例，下面给出了相关的安装命令：<br>
<pre class="prettyprint">sudo apt-get update<br>
sudo apt-get -y install skopeo<br>
sudo apt-get -y install jq<br>
</pre><br>
<h3>复制镜像</h3>作为示例的是 Nginx 的镜像。首先使用 <code class="prettyprint">skopeo copy</code> 命令把 Nginx 镜像转换成 OCI 镜像的格式。<code class="prettyprint">skopeo copy</code> 的源 <code class="prettyprint">docker://nginx</code> 表示 Docker Hub 上的标签为 <code class="prettyprint">latest</code> 的 Nginx 镜像，目标 <code class="prettyprint">oci:local_nginx</code> 的前缀 <code class="prettyprint">oci:</code> 表示 OCI 镜像格式，<code class="prettyprint">local_nginx</code> 是本地目录的名称。<br><br>
<pre class="prettyprint">skopeo copy docker://nginx oci:local_nginx<br>
</pre><br>
下面是该命令的输出结果。<br>
<pre class="prettyprint">Getting image source signatures<br>
Copying blob eff15d958d66 done  <br>
Copying blob 1e5351450a59 done  <br>
Copying blob 2df63e6ce2be done  <br>
Copying blob 9171c7ae368c done  <br>
Copying blob 020f975acd28 done  <br>
Copying blob 266f639b35ad done<br>
Copying config 9d446b871e done  <br>
Writing manifest to image destination<br>
Storing signatures<br>
</pre><br>
该命令运行完成之后，Nginx 镜像的内容就以 OCI 镜像规范的格式保存到了本地。<br>
<h3>镜像的内容</h3>转到 <code class="prettyprint">local_nginx</code> 目录，使用 <code class="prettyprint">tree</code> 命令查看该目录的内容。<br><br>
<pre class="prettyprint">tree --du .<br>
</pre><br>
在该目录中，根目录下有两个文件 <code class="prettyprint">oci-layout</code> 和 <code class="prettyprint">index.json</code>。目录 <code class="prettyprint">blobs</code> 中包含了文件的实际内容，使用的是内容寻址的方式。目录名称 <code class="prettyprint">sha256</code> 表示内容摘要的算法，对应于 SHA-256。文件名是摘要。<br>
<pre class="prettyprint">.├── [   56737397]  blobs│   └── [   56733301]  sha256│       ├── [        668]  020f975acd28936c7ff43827238aed4771d14235dc983389ec149811f7e0b7cf│       ├── [   25347687]  1e5351450a593c3a3d7a5104f93c8b80d8dc00c827158cb3a5bf985916ea3f75│       ├── [       1394]  266f639b35ad602ee76c3b4d4cf88285a50adf8f561d8d96d331db732fe16982│       ├── [        602]  2df63e6ce2be0b3cefd3e659558e92b8085f032db96828343ec9cf0b7d4409fe│       ├── [        895]  9171c7ae368c6ca24dae913fce356801f624f656360c78ca956a92c3f0fe0ec7│       ├── [       6566]  9d446b871e5882110acf8dc0ab827425b8d25184f9426b12b2073186a0b2cdce│       ├── [       1126]  b77780a5c0973c290799dea52ccbc975f61954907de8108d6f99e65a44fa7623│       └── [   31370267]  eff15d958d664f0874d16aee393cc44387031ee0a68ef8542d0056c747f378e8├── [        187]  index.json└── [         31]  oci-layout    56741711 bytes used in 2 directories, 10 files<br>
</pre><br>
<code class="prettyprint">oci-layout</code> 是 OCI 镜像规范的占位符，其中的内容如下所示。<br>
<pre class="prettyprint">&#123;"imageLayoutVersion": "1.0.0"&#125; <br>
</pre><br>
<h3>镜像索引文件</h3><code class="prettyprint">index.json</code> 是 OCI 镜像索引文件，对应的规范是 OCI Image Index Specification，使用媒体类型 <code class="prettyprint">application/vnd.oci.image.index.v1+json</code>。<br>
<br>查看该文件的内容并使用 <code class="prettyprint">jq</code> 进行格式化。<br>
<pre class="prettyprint">cat index.json | jq<br>
</pre><br>
输出的内容如下所示：<br>
<pre class="prettyprint">&#123;<br>
"schemaVersion": 2,<br>
"manifests": [<br>
&#123;<br>
  "mediaType": "application/vnd.oci.image.manifest.v1+json",<br>
  "digest": "sha256:b77780a5c0973c290799dea52ccbc975f61954907de8108d6f99e65a44fa7623",<br>
  "size": 1126<br>
&#125;<br>
]<br>
&#125; <br>
</pre><br>
在 <code class="prettyprint">manifests</code> 中包含多个镜像清单文件的引用。每个清单文件通常对应一个平台。这里只有一个清单文件。每个清单描述的 <code class="prettyprint">digest</code> 表示文件的摘要，在 <code class="prettyprint">blobs</code> 目录中可以找到对应的文件。<br>
<h3>镜像清单文件</h3>清单文件对应的规范是 OCI Image Manifest Specification，使用媒体类型 <code class="prettyprint">application/vnd.oci.image.manifest.v1+json</code>。<br>
<br>把清单文件的 <code class="prettyprint">digest</code> 值转换成路径，就可以查看清单文件的内容。<code class="prettyprint">sha256:b77780a5c0973c290799dea52ccbc975f61954907de8108d6f99e65a44fa7623</code> 被转换成路径 <code class="prettyprint">blobs/sha256/b77780a5c0973c290799dea52ccbc975f61954907de8108d6f99e65a44fa762</code>。<br>
<pre class="prettyprint">cat blobs/sha256/b77780a5c0973c290799dea52ccbc975f61954907de8108d6f99e65a44fa7623 | jq<br>
</pre><br>
下面是清单文件的内容。<br>
<pre class="prettyprint">&#123;<br>
"schemaVersion": 2,<br>
"config": &#123;<br>
"mediaType": "application/vnd.oci.image.config.v1+json",<br>
"digest": "sha256:9d446b871e5882110acf8dc0ab827425b8d25184f9426b12b2073186a0b2cdce",<br>
"size": 6566<br>
&#125;,<br>
"layers": [<br>
&#123;<br>
  "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",<br>
  "digest": "sha256:eff15d958d664f0874d16aee393cc44387031ee0a68ef8542d0056c747f378e8",<br>
  "size": 31370267<br>
&#125;,<br>
&#123;<br>
  "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",<br>
  "digest": "sha256:1e5351450a593c3a3d7a5104f93c8b80d8dc00c827158cb3a5bf985916ea3f75",<br>
  "size": 25347687<br>
&#125;,<br>
&#123;<br>
  "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",<br>
  "digest": "sha256:2df63e6ce2be0b3cefd3e659558e92b8085f032db96828343ec9cf0b7d4409fe",<br>
  "size": 602<br>
&#125;,<br>
&#123;<br>
  "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",<br>
  "digest": "sha256:9171c7ae368c6ca24dae913fce356801f624f656360c78ca956a92c3f0fe0ec7",<br>
  "size": 895<br>
&#125;,<br>
&#123;<br>
  "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",<br>
  "digest": "sha256:020f975acd28936c7ff43827238aed4771d14235dc983389ec149811f7e0b7cf",<br>
  "size": 668<br>
&#125;,<br>
&#123;<br>
  "mediaType": "application/vnd.oci.image.layer.v1.tar+gzip",<br>
  "digest": "sha256:266f639b35ad602ee76c3b4d4cf88285a50adf8f561d8d96d331db732fe16982",<br>
  "size": 1394<br>
&#125;<br>
]<br>
&#125; <br>
</pre><br>
在清单文件中，<code class="prettyprint">config</code> 是镜像的配置文件，<code class="prettyprint">layers</code> 是镜像中的层。<code class="prettyprint">mediaType</code> 说明了文件的媒体类型。比如，配置文件使用的是 JSON 格式；每个层则是 gzip 压缩的 tar 文件。<br>
<h3>镜像配置文件</h3>镜像配置文件对应的规范是 OCI Image Configuration，使用媒体类型 <code class="prettyprint">application/vnd.oci.image.config.v1+json</code>。<br>
<br>可以按照同样的方式来查看配置文件的内容。<br>
<pre class="prettyprint">cat blobs/sha256/9d446b871e5882110acf8dc0ab827425b8d25184f9426b12b2073186a0b2cdce | jq<br>
</pre><br>
下面是配置文件的完整内容。<br>
<pre class="prettyprint">&#123;<br>
"created": "2021-11-17T10:38:14.652464384Z",<br>
"architecture": "amd64",<br>
"os": "linux",<br>
"config": &#123;<br>
"ExposedPorts": &#123;<br>
  "80/tcp": &#123;&#125;<br>
&#125;,<br>
"Env": [<br>
  "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",<br>
  "NGINX_VERSION=1.21.4",<br>
  "NJS_VERSION=0.7.0",<br>
  "PKG_RELEASE=1~bullseye"<br>
],<br>
"Entrypoint": [<br>
  "/docker-entrypoint.sh"<br>
],<br>
"Cmd": [<br>
  "nginx",<br>
  "-g",<br>
  "daemon off;"<br>
],<br>
"Labels": &#123;<br>
  "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"<br>
&#125;,<br>
"StopSignal": "SIGQUIT"<br>
&#125;,<br>
"rootfs": &#123;<br>
"type": "layers",<br>
"diff_ids": [<br>
  "sha256:e1bbcf243d0e7387fbfe5116a485426f90d3ddeb0b1738dca4e3502b6743b325",<br>
  "sha256:37380c5830feb5d6829188be41a4ea0654eb5c4632f03ef093ecc182acf40e8a",<br>
  "sha256:ff4c727794302b5a0ee4dadfaac8d1233950ce9a07d76eb3b498efa70b7517e4",<br>
  "sha256:49eeddd2150fbd14433ec1f01dbf6b23ea6cf581a50635554826ad93ce040b68",<br>
  "sha256:1e8ad06c81b6baf629988756d90fd27c14285da4d9bf57179570febddc492087",<br>
  "sha256:8525cde30b227bb5b03deb41bda41deb85d740b834be61a69ead59d840f07c13"<br>
]<br>
&#125;,<br>
"history": [<br>
&#123;<br>
  "created": "2021-11-17T02:20:41.91188934Z",<br>
  "created_by": "/bin/sh -c #(nop) ADD file:a2405ebb9892d98be2eb585f6121864d12b3fd983ebf15e5f0b7486e106a79c6 in / "<br>
&#125;,<br>
&#123;<br>
  "created": "2021-11-17T02:20:42.315994925Z",<br>
  "created_by": "/bin/sh -c #(nop)  CMD [\"bash\"]",<br>
  "empty_layer": true<br>
&#125;,<br>
&#123;<br>
  "created": "2021-11-17T10:37:39.564148274Z",<br>
  "created_by": "/bin/sh -c #(nop)  LABEL maintainer=NGINX Docker Maintainers <docker-maint@nginx.com>",<br>
  "empty_layer": true<br>
&#125;,<br>
&#123;<br>
  "created": "2021-11-17T10:37:39.941485145Z",<br>
  "created_by": "/bin/sh -c #(nop)  ENV NGINX_VERSION=1.21.4",<br>
  "empty_layer": true<br>
&#125;,<br>
&#123;<br>
  "created": "2021-11-17T10:37:40.256097748Z",<br>
  "created_by": "/bin/sh -c #(nop)  ENV NJS_VERSION=0.7.0",<br>
  "empty_layer": true<br>
&#125;,<br>
&#123;<br>
  "created": "2021-11-17T10:37:40.480423114Z",<br>
  "created_by": "/bin/sh -c #(nop)  ENV PKG_RELEASE=1~bullseye",<br>
  "empty_layer": true<br>
&#125;,<br>
&#123;<br>
  "created": "2021-11-17T10:38:11.674629445Z",<br>
  "created_by": "/bin/sh -c set -x     && addgroup --system --gid 101 nginx     && adduser --system --disabled-login --ingroup nginx --no-create-home --home /nonexistent --gecos \"nginx user\" --shell /bin/false --uid 101 nginx     && apt-get update     && apt-get install --no-install-recommends --no-install-suggests -y gnupg1 ca-certificates     &&     NGINX_GPGKEY=573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62;     found='';     for server in         hkp://keyserver.ubuntu.com:80         pgp.mit.edu     ; do         echo \"Fetching GPG key $NGINX_GPGKEY from $server\";         apt-key adv --keyserver \"$server\" --keyserver-options timeout=10 --recv-keys \"$NGINX_GPGKEY\" && found=yes && break;     done;     test -z \"$found\" && echo >&2 \"error: failed to fetch GPG key $NGINX_GPGKEY\" && exit 1;     apt-get remove --purge --auto-remove -y gnupg1 && rm -rf /var/lib/apt/lists/*     && dpkgArch=\"$(dpkg --print-architecture)\"     && nginxPackages=\"         nginx=$&#123;NGINX_VERSION&#125;-$&#123;PKG_RELEASE&#125;         nginx-module-xslt=$&#123;NGINX_VERSION&#125;-$&#123;PKG_RELEASE&#125;         nginx-module-geoip=$&#123;NGINX_VERSION&#125;-$&#123;PKG_RELEASE&#125;         nginx-module-image-filter=$&#123;NGINX_VERSION&#125;-$&#123;PKG_RELEASE&#125;         nginx-module-njs=$&#123;NGINX_VERSION&#125;+$&#123;NJS_VERSION&#125;-$&#123;PKG_RELEASE&#125;     \"     && case \"$dpkgArch\" in         amd64|arm64)             echo \"deb https://nginx.org/packages/mainline/debian/ bullseye nginx\" >> /etc/apt/sources.list.d/nginx.list             && apt-get update             ;;         *)             echo \"deb-src https://nginx.org/packages/mainline/debian/ bullseye nginx\" >> /etc/apt/sources.list.d/nginx.list                         && tempDir=\"$(mktemp -d)\"             && chmod 777 \"$tempDir\"                         && savedAptMark=\"$(apt-mark showmanual)\"                         && apt-get update             && apt-get build-dep -y $nginxPackages             && (                 cd \"$tempDir\"                 && DEB_BUILD_OPTIONS=\"nocheck parallel=$(nproc)\"                     apt-get source --compile $nginxPackages             )                         && apt-mark showmanual | xargs apt-mark auto > /dev/null             && &#123; [ -z \"$savedAptMark\" ] || apt-mark manual $savedAptMark; &#125;                         && ls -lAFh \"$tempDir\"             && ( cd \"$tempDir\" && dpkg-scanpackages . > Packages )             && grep '^Package: ' \"$tempDir/Packages\"             && echo \"deb [ trusted=yes ] file://$tempDir ./\" > /etc/apt/sources.list.d/temp.list             && apt-get -o Acquire::GzipIndexes=false update             ;;     esac         && apt-get install --no-install-recommends --no-install-suggests -y                         $nginxPackages                         gettext-base                         curl     && apt-get remove --purge --auto-remove -y && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/nginx.list         && if [ -n \"$tempDir\" ]; then         apt-get purge -y --auto-remove         && rm -rf \"$tempDir\" /etc/apt/sources.list.d/temp.list;     fi     && ln -sf /dev/stdout /var/log/nginx/access.log     && ln -sf /dev/stderr /var/log/nginx/error.log     && mkdir /docker-entrypoint.d"<br>
&#125;,<br>
&#123;<br>
  "created": "2021-11-17T10:38:12.409891183Z",<br>
  "created_by": "/bin/sh -c #(nop) COPY file:65504f71f5855ca017fb64d502ce873a31b2e0decd75297a8fb0a287f97acf92 in / "<br>
&#125;,<br>
&#123;<br>
  "created": "2021-11-17T10:38:12.732754797Z",<br>
  "created_by": "/bin/sh -c #(nop) COPY file:0b866ff3fc1ef5b03c4e6c8c513ae014f691fb05d530257dfffd07035c1b75da in /docker-entrypoint.d "<br>
&#125;,<br>
&#123;<br>
  "created": "2021-11-17T10:38:13.174315469Z",<br>
  "created_by": "/bin/sh -c #(nop) COPY file:0fd5fca330dcd6a7de297435e32af634f29f7132ed0550d342cad9fd20158258 in /docker-entrypoint.d "<br>
&#125;,<br>
&#123;<br>
  "created": "2021-11-17T10:38:13.510082553Z",<br>
  "created_by": "/bin/sh -c #(nop) COPY file:09a214a3e07c919af2fb2d7c749ccbc446b8c10eb217366e5a65640ee9edcc25 in /docker-entrypoint.d "<br>
&#125;,<br>
&#123;<br>
  "created": "2021-11-17T10:38:13.827956179Z",<br>
  "created_by": "/bin/sh -c #(nop)  ENTRYPOINT [\"/docker-entrypoint.sh\"]",<br>
  "empty_layer": true<br>
&#125;,<br>
&#123;<br>
  "created": "2021-11-17T10:38:14.069756108Z",<br>
  "created_by": "/bin/sh -c #(nop)  EXPOSE 80",<br>
  "empty_layer": true<br>
&#125;,<br>
&#123;<br>
  "created": "2021-11-17T10:38:14.348754639Z",<br>
  "created_by": "/bin/sh -c #(nop)  STOPSIGNAL SIGQUIT",<br>
  "empty_layer": true<br>
&#125;,<br>
&#123;<br>
  "created": "2021-11-17T10:38:14.652464384Z",<br>
  "created_by": "/bin/sh -c #(nop)  CMD [\"nginx\" \"-g\" \"daemon off;\"]",<br>
  "empty_layer": true<br>
&#125;<br>
]<br>
&#125; <br>
</pre><br>
这个配置的内容比较多，介绍几个重要的属性：<br>
<ul><li><code class="prettyprint">config</code> 表示从镜像运行容器时的参数。比如，<code class="prettyprint">Env</code> 表示的环境变量，<code class="prettyprint">Entrypoint</code> 表示的入口命令，<code class="prettyprint">ExposedPorts</code> 表示的开放端口。</li><li><code class="prettyprint">rootfs</code> 表示镜像的文件系统中包含的层。</li><li><code class="prettyprint">history</code> 表示每个层的构建历史。有些历史记录对象的 <code class="prettyprint">empty_layer</code> 的值为 <code class="prettyprint">true</code>，表示该历史记录并没有对层进行修改，而只是修改了配置。比如倒数第三条历史记录由 <code class="prettyprint">EXPOSE 80</code> 指令产生，只是修改了配置。</li></ul><br>
<br><h3>镜像中的层</h3>下面查看一下层的内容。前面提到过，层的格式是 gzip 压缩的 tar 文件。下面的命令解压缩一个层的内容到 <code class="prettyprint">~/files</code> 目录。<br><br>
<pre class="prettyprint">tar -xf blobs/sha256/266f639b35ad602ee76c3b4d4cf88285a50adf8f561d8d96d331db732fe16982 -C ~/files<br>
</pre><br>
查看 <code class="prettyprint">~/files</code>目录的内容可以发现，这个层中仅包含一个路径为 <code class="prettyprint">/docker-entrypoint.d/30-tune-worker-processes.sh</code> 的文件。<br>
<pre class="prettyprint">$ tree --du ~/files/<br>
/home/ubuntu/files/<br>
└── [       8709]  docker-entrypoint.d<br>
└── [       4613]  30-tune-worker-processes.sh<br>
<br>
   12805 bytes used in 1 directory, 1 file<br>
</pre><br>
与 Nginx 镜像的 Dockerfile 对比之后可以发现，这个层是由下面的 <code class="prettyprint">COPY</code> 指令生成的。<br>
<pre class="prettyprint">COPY 30-tune-worker-processes.sh /docker-entrypoint.d<br>
</pre><br>
这样就建立起来了 Dockerfile 的指令与镜像的层的对应关系。<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/HFjJGPzt8qoG90w13siu3A" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/HFjJGPzt8qoG90w13siu3A</a>
                                
                                                              
</div>
            