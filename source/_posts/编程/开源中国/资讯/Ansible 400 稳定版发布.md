
---
title: 'Ansible 4.0.0 稳定版发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5258'
author: 开源中国
comments: false
date: Wed, 26 May 2021 08:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5258'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Red Hat 已于上周<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgroups.google.com%2Fg%2Fansible-devel%2Fc%2FAeF2En1RGI8" target="_blank">发布</a>了 Ansible 4.0，并表示此次更新基于 ansible-core-2.11.x 软件包，对于 Ansible 3 使用的软件包来说是一次重大更新。Ansible 3 基于 Ansible Base 2.10.x，所以 4 和 3 的 core playbook 语言可能会向后不兼容。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.ansible.com%2Fansible%2Fdevel%2Fporting_guides%2Fporting_guide_4.html" target="_blank">详情查看迁移指南</a>。</p> 
<p><strong>获取新版本</strong></p> 
<p>由于 PIP 的限制，如果希望从 Ansible 3（或者更早版本）进行升级，则需要在安装 Ansible 4 之前卸载 Ansible 和 Ansible Base。</p> 
<pre><code>$ pip uninstall ansible ansible-base
$ pip install ansible==4.0.0 --user</code></pre> 
<p>Ansible 4.0.0：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpypi.python.org%2Fpackages%2Fsource%2Fa%2Fansible%2Fansible-4.0.0.tar.gz" target="_blank">https://pypi.python.org/packages/source/a/ansible/ansible-4.0.0.tar.gz</a></p> 
<p><strong>新特性</strong></p> 
<ul> 
 <li>此版本基于 Ansible Core 2.11，它是 ansible-core 软件包的一次重大更新，因此可能包含对 playbook 语言和命令行 line0 程序的向后不兼容的变化。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.ansible.com%2Fansible%2Fdevel%2Fporting_guides%2Fporting_guide_4.html" target="_blank">详情查看迁移指南</a>。</li> 
 <li>添加一种以编程方式安装 Ansible 软件包版本的方法</li> 
</ul> 
<pre><code class="language-python">python -c 'from ansible_collections.ansible_release import
ansible_version; print(ansible_version)'
4.0.0</code></pre> 
<p>官方表示，由于 Ansible 4 已发布，因此对 Ansible 3 的更新即将停止。新的次要版本大约每三周发布一次（Ansible 4.1.0、Ansible 4.2.0 等）。这些版本将包含错误修复和新功能，但不存在向后不兼容的情况。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fansible-community%2Fansible-build-data%2Fblob%2Fmain%2F4%2FCHANGELOG-v4.rst" target="_blank">更新日志</a></p>
                                        </div>
                                      
</div>
            