
---
title: 'Midway v2.12.1 发布，新增 Axios 组件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8199'
author: 开源中国
comments: false
date: Sun, 01 Aug 2021 18:03:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8199'
---

<div>   
<div class="content">
                                                                                            <h2>Features</h2> 
<h3>1、新增 Axios 组件</h3> 
<p>提供一个 axios 组件，用于发送 http 请求。</p> 
<p>接口保持和 axios 一致，处理了作用域相关的问题。</p> 
<p>使用示例：</p> 
<pre>import &#123; HttpService &#125; from '@midwayjs/axios';

@Provide()
export class UserService &#123;

  @Inject()
  httpService: HttpService;
  
  async invoke() &#123;
  
    const url = 'https://api.github.com/users/octocat/orgs';
    const result = await this.httpService.get(url);
    // TODO resut
  &#125;
&#125;</pre> 
<p>具体请查看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Fmidwayjs%2Fmidway_v2%2Faxios" target="_blank">axios 文档</a>。</p> 
<h2>Bugfix</h2> 
<h3>1、处理默认 listen hostname 可能引起 502 的问题</h3> 
<p>具体见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmidwayjs%2Fmidway%2Fissues%2F1195" target="_blank">issue#1195</a></p> 
<p>新版本将参数分开，恢复了默认行为。</p> 
<h3>2、bootstrap 新增 preloadModules 透传</h3> 
<p><code>preloadModules</code> 启动参数是用于 ncc 构建的预留，之前未透传，在一些极端情况下需要使用，比如 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmidwayjs%2Fmidway%2Fissues%2F1193" target="_blank">issue#1193</a>。</p> 
<p>新版本增加了启动参数的透传。</p>
                                        </div>
                                      
</div>
            