
---
title: 'Midway v2.12.5 发布，Node.js 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9538'
author: 开源中国
comments: false
date: Wed, 18 Aug 2021 18:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9538'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p>Midway 是一个适用于构建 Serverless 服务，传统应用、微服务，小程序后端的 Node.js 框架。</p> 
 <h2>Features</h2> 
 <h3>1、支持 onConfigLoad 生命周期</h3> 
 <p>在 Configuration 中新增了一个 <code>onConfigLoad</code> 方法，用于替代原有的 bootstrap 中的 before 方法，可以用做配置异步加载。</p> 
 <p>示例：</p> 
 <pre>@Configuration(&#123;
  importConfigs: [
    join(__dirname, './config/'),
  ]
&#125;)
export class ContainerLifeCycle &#123;
  
  async onConfigLoad(container: IMidwayContainer) &#123;
    // 这里你可以修改全局配置
    const remoteConfigService = await container.getAsync(RemoteConfigService);
    const remoteConfig = await remoteConfigService.getData();
    
    // 这里的返回值会和全局的 config 做合并
    return &#123;
      data: remoteConfig
    &#125;;
  &#125;
&#125; </pre> 
 <p>文档已更新。</p> 
 <h3>2、Task 增加并发配置</h3> 
 <p>感谢社区 @<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FEliYao" target="_blank">EliYao</a> 提供此 PR。</p> 
 <p>开放了一个 bull 中并发创建任务的配置，默认为 1。</p> 
 <pre>export const task = &#123;
concurrency: 1
&#125;
</pre> 
 <h2>Bugfix</h2> 
 <h3>1、修复组件分环境加载报错的问题</h3> 
 <p>在帮用户排查问题时发现，组件在使用环境过滤时，会出现未找到组件Configuration 的错误，原因为组件被过滤后，组件的类定义依旧在容器中（reuqire 时执行）。</p> 
 <p>新版本修复了这个问题。</p> 
 <p>出现场景：swagger 组件</p> 
 <h3>2、处理 aspect 拦截求链式调用的问题</h3> 
 <p>感谢社区 @<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fchenzhaozheng" target="_blank">chenzhaozheng</a> 提供此 PR。</p> 
 <p>现在，在被拦截的对象调用其他的方法 ，依旧会被正确拦截。</p> 
 <h3>3、处理 egg-layer 中 unix socket 转发中文的问题</h3> 
 <p>感谢社区 @<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdreamer2q" target="_blank">dreamer2q</a> 提供此 PR。</p> 
 <p>在 egg-layer 中，使用了 unix socket 转发的方案，在转发 path 中包含中文字符时，会出现 unsupport 的报错。新版本修复了该问题。</p> 
</div>
                                        </div>
                                      
</div>
            