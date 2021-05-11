
---
title: 'Containerd 1.5 发布：重磅支持 docker-compose！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/dc657bb0-5f30-4aba-99f8-42f32f7be3e2.gif'
author: 开源中国
comments: false
date: Tue, 11 May 2021 14:18:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/dc657bb0-5f30-4aba-99f8-42f32f7be3e2.gif'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img src="https://oscimg.oschina.net/oscnet/dc657bb0-5f30-4aba-99f8-42f32f7be3e2.gif" referrerpolicy="no-referrer"></p> 
<p>2021 年 5 月 4 日，Containerd 1.5 正式发布[1]，该版本默认启用了 <code>OCIcrypt</code> 解密功能，并引入了对 <code>NRI</code>、<code>zstd</code> 和 <code>FreeBSD jails</code> 的支持，同时还简化了对 Containerd 的贡献流程。下面就来看看具体更新了哪些功能吧。</p> 
<h2>默认 OCIcrypt 解密</h2> 
<p>Containerd 从 1.3 开始就支持从加密的镜像中运行容器，但没有作为默认启用的选项，直到 1.5 版本才默认启用，具体用法请参考文档[2]。</p> 
<p>需要注意的是，必须安装二进制文件 <code>ctd-decoder</code> 才能解密 OCIcrypt 镜像，该二进制文件包含在 cri-containerd-cni-1.5.0-linux-amd64.tar.gz[3] 中，但不包含在 <code>containerd-1.5.0-linux-amd64.tar.gz</code> 中。另外，<code>OCIcrypt</code> 并不适用于 Docker，因为 Docker 目前并没有使用 Containerd 来管理镜像。</p> 
<h2>NRI: Node Resource Interface</h2> 
<p>NRI(Node Resource Interface)[4] 即<strong>节点资源接口</strong>，类似于 <code>CRI</code>，但 <code>NRI</code> 可用于非网络资源，例如 GPU 调度限制和内存配额。具体用法可参考 NRI 示例代码[5]。</p> 
<h2>zstd 压缩算法</h2> 
<p>除了 gzip 之外，Containerd 现在还支持 zstd[6] 镜像压缩算法，压缩速度比 <code>gzip</code> 快好几倍，具体通过 github.com/klauspost/compress/zstd[7] 来实现。关于 zstd 的性能测试结果请参考zstd 官方文档[8]。</p> 
<h2>支持 FreeBSD</h2> 
<p>Containerd 从 1.5 版本开始实验性地支持 FreeBSD 操作系统，可以使用 FreeBSD jails[9] 运行一个兼容的 <code>OCI</code> 运行时，例如 runj[10]。同时还支持 <code>ZFS</code> 的快照管理，未来版本可能也会支持 unionfs[11]。</p> 
<p><img src="https://oscimg.oschina.net/oscnet/2934d1d0-53c3-4504-883a-1fac42a63779.png" referrerpolicy="no-referrer"></p> 
<h2>简化贡献流程</h2> 
<p>CRI 插件仓库[12] 现已合并到 Containerd 主仓库[13]中，对用户来说没有明显变化，只是简化了开发者对 Containerd 的贡献流程。</p> 
<h2>nerdctl</h2> 
<p>nerdctl[14] 是一个与 Docker 兼容的 CLI，例如：</p> 
<pre><code>$ nerdctl run -d --name nginx -p 8080:80 --restart=always nginx
</code></pre> 
<p>但 <code>nerdctl</code> 的目标并不是单纯地复制 docker 的功能，它还实现了很多 docker 不具备的功能，例如延迟拉取镜像（lazy-pulling[15])、镜像加密（imgcrypt[16]）等。</p> 
<p>nerdctl 在上个月作为非核心子项目加入了 Containerd 组织，详情请参考<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzU1MzY4NzQ1OA%3D%3D%26mid%3D2247494425%26idx%3D1%26sn%3Dc5d684fc4a45156499cd052009a82e9c%26chksm%3Dfbedabd4cc9a22c2c2255159846ebcbd1df0f7a212ef2f77da2cfb976fc631d8e12357eee0a2%26scene%3D21%23wechat_redirect" target="_blank">终于可以像使用 Docker 一样丝滑地使用 Containerd 了！</a></p> 
<p>现在 nerdctl 还推出了一个爆炸性功能：<strong>直接兼容 docker-compose 的语法</strong>！也就是说，可以直接通过 docker-compose.yaml 启动容器：</p> 
<pre><code>$ nerdctl compose -f docker-compose.yaml up
</code></pre> 
<p>求 Docker 此时内心的阴影面积。。</p> 
<p>本来 Docker 在 <code>Kubernetes</code> 社区的地位就在急剧下滑，现在 Containerd 易用性的空缺也被 <code>nerdctl</code> 填补上了，连 docker-compose 也能兼容了，如今 Docker 就更不受待见了。虽说廋死的骆驼比马大，但 Docker 的辉煌时代终究一去不复返了。</p> 
<h3>脚注</h3> 
<p>[1] Containerd 1.5 正式发布: <em>https://github.com/containerd/containerd/releases/tag/v1.5.0</em></p> 
<p>[2] 参考文档: <em>https://github.com/containerd/containerd/blob/v1.5.0-rc.2/docs/cri/decryption.md</em></p> 
<p>[3] cri-containerd-cni-1.5.0-linux-amd64.tar.gz: <em>https://github.com/containerd/containerd/releases</em></p> 
<p>[4] NRI(Node Resource Interface): <em>https://github.com/containerd/nri</em></p> 
<p>[5] NRI 示例代码: <em>https://github.com/containerd/nri#sample-plugin</em></p> 
<p>[6] zstd: <em>https://github.com/containerd/containerd/pull/4809</em></p> 
<p>[7] github.com/klauspost/compress/zstd: <em>https://github.com/klauspost/compress/tree/master/zstd</em></p> 
<p>[8] zstd 官方文档: <em>https://github.com/klauspost/compress/blob/master/zstd/README.md</em></p> 
<p>[9] FreeBSD jails: <em>https://en.wikipedia.org/wiki/FreeBSD_jail</em></p> 
<p>[10] runj: <em>https://github.com/samuelkarp/runj</em></p> 
<p>[11] unionfs: <em>https://www.freebsd.org/cgi/man.cgi?query=unionfs&sektion=8&manpath=freebsd-release-ports</em></p> 
<p>[12] CRI 插件仓库: <em>https://github.com/containerd/cri</em></p> 
<p>[13] Containerd 主仓库: <em>https://github.com/containerd/cri</em></p> 
<p>[14] nerdctl: <em>https://github.com/containerd/nerdctl</em></p> 
<p>[15] lazy-pulling: <em>https://github.com/containerd/nerdctl/blob/master/docs/stargz.md</em></p> 
<p>[16] imgcrypt: <em>https://github.com/containerd/nerdctl/blob/master/docs/ocicrypt.md</em></p>
                                        </div>
                                      
</div>
            