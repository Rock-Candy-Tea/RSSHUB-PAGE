
---
title: 'Beerus 1.1.7 来啦，带来了 5 大特性'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1227'
author: 开源中国
comments: false
date: Mon, 27 Dec 2021 11:56:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1227'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p>Beerus是一个用go 开发的web解决方案，包含一个web框架，一个数据库操作框架，以及正在规划中的RPC框架，未来还会开发更多的组件。</p> 
 <h2>本次更新的点如下</h2> 
 <ul> 
  <li>支持形参接收参数</li> 
  <li>可以在 JSON 模式和非 JSON 模式之间切换</li> 
  <li>加入错误处理机制</li> 
  <li>拦截器更好的兼容 JSON 和非 JSON 模式</li> 
  <li>ToStruct 和 Validation 函数 简化了一下，只需要传入指针，不再需要传值</li> 
 </ul> 
 <h2>用形参接收请求参数</h2> 
 <p>只需要将定义好的 struct 加入到路由函数的参数列表即可</p> 
 <pre><code class="language-go">route.GET("/test", func(param DemoParam) &#123;

&#125;)

type DemoParam struct &#123;
    Name string `field:"name"`
    Age int `field:"age"`
    Friends []string
&#125;</code></pre> 
 <p>前端请求这个路由的时候，参数会被自动提取到 param 中</p> 
 <h2>在 JSON 模式和非 JSON 模式之间切换</h2> 
 <p><strong>默认就是 JSON 模式，JSON 模式有以下特性</strong></p> 
 <ul> 
  <li>必须有返回值，返回值数量 1-2 个，如果只有一个：那么必须是返回要响应的数据，如果有两个：那么第一个必须是要响应的数据，第二个必须是 error 类型</li> 
  <li>不需要手工调用 Validation 函数来实现参数验证，beerus 会自动处理</li> 
 </ul> 
 <p><strong>一个返回值的示例</strong></p> 
 <p>返回类型可以是 struct ，map ，数组，这里为了演示方便就用的 map</p> 
 <pre><code class="language-go">route.GET("/test", func(param DemoParam, req commons.BeeRequest, res commons.BeeResponse) map[string]string&#123;

    msg := make(map[string]string)
    msg["msg"] = "hello word"
  
    // 直接返回即可，beerus 会自动将他转成 json 响应给前端
    return msg
&#125;)</code></pre> 
 <p><strong>两个返回值的示例</strong></p> 
 <p>第一个返回值的类型同上，第二个返回值必须是 error 类型</p> 
 <pre><code class="language-go">route.GET("/test", func(param DemoParam, req commons.BeeRequest, res commons.BeeResponse) (map[string]string, error) &#123;
  
    if xxx &#123;
      return nil, errors.New("错误提示信息")
    &#125;
  
    msg := make(map[string]string)
    msg["msg"] = "hello word"
  
    // 直接返回即可，beerus 会自动将他转成 json 响应给前端
    return msg, nil
&#125;)</code></pre> 
 <p><strong>关闭 JSON 模式，很简单，只需要在创建路由前 执行以下代码</strong></p> 
 <pre><code class="language-go">route.JsonMode = false</code></pre> 
 <p>JSON 模式一旦关闭，那么 JSON 模式的特性将会全部失效，路由函数不可以有返回值，我们需要手动调用 Validation 函数实现参数验证，手动调用 res.SendXXX 函数实现数据响应</p> 
 <pre><code class="language-go">route.GET("/test", func(param DemoParam, req commons.BeeRequest, res commons.BeeResponse) &#123;
    
    var result = params.Validation(req, &param)
    
    // 当返回的不是 SUCCESS ，就说明验证没通过
    if result != params.SUCCESS &#123;
        // 这里可以自己选择合适的 SendXXX 函数
        res.SendErrorMsg(1128, result)
        return
    &#125;
    
    // 这里可以自己选择合适的 SendXXX 函数
    res.SendJson(`&#123;"msg":"hello word"&#125;`)
    
&#125;)</code></pre> 
 <h2>错误处理机制</h2> 
 <p>看了上面的 JSON 模式，大家应该猜到了，错误处理机制就是在路由函数上设置第二个返回值，把我们需要响应给前端的错误提示信息 通过第二个返回值返回即可</p> 
 <pre><code class="language-go">route.GET("/test", func(param DemoParam, req commons.BeeRequest, res commons.BeeResponse) (map[string]string, error) &#123;
  
    if xxx &#123;
      return nil, errors.New("错误提示信息")
    &#125;
  
    msg := make(map[string]string)
    msg["msg"] = "hello word"
  
    // 直接返回即可，beerus 会自动将他转成 json 响应给前端
    return msg, nil
&#125;)</code></pre> 
 <h2>拦截器更好的兼容 JSON 和非 JSON 模式</h2> 
 <p>之前的拦截器是，如果放行 就返回 SUCCESS 常量，否则返回提示信息；这种做法有一个缺陷，就是只能以 JSON 的形式 给前端发送提示，如果开发者不想用 JSON 跟前端交互，那么这种设计将会是一个缺陷。</p> 
 <p>现在改成了，拦截器返回一个 bool ，如果放行就返回 true ，否则返回 false ，<strong>但是有一个注意点：如果你要返回 false ，那么就必须先调用 res.SendXXX 函数给前端一个响应，不然本次请求会被阻塞到超时，对性能造成影响</strong>*</p> 
 <pre><code class="language-go">func CreateInterceptor() &#123;
  route.AddInterceptor("/example/*", loginInterceptorBefore)
&#125;

func loginInterceptorBefore(req *commons.BeeRequest, res *commons.BeeResponse) bool &#123;
  res.
  SetHeader("hello", "hello word").
  SetHeader("hello2", "word2")

  log.Println("exec interceptor")
  return true
&#125;</code></pre> 
 <h2>ToStruct 和 Validation 函数 简化了一下</h2> 
 <p>以前调用 ToStruct 需要这样，传入指针 和值，有一点麻烦</p> 
 <pre><code class="language-go">param := DemoParam&#123;&#125;
params.ToStruct(req, &param, param)</code></pre> 
 <p>现在改成了这样，只需要传指针</p> 
 <pre><code class="language-go">param := DemoParam&#123;&#125;
params.ToStruct(req, &param)</code></pre> 
 <p>虽然，有了形参接收参数的功能以后，这种写法可能会被渐渐淘汰掉，但是依然会有被使用的可能性，所以暂时保留了下来，并做了一个优化。</p> 
 <hr> 
 <p>以前调用 Validation 需要这样，传入指针和值，有一点麻烦</p> 
 <pre><code class="language-go">var result = params.Validation(req, &param, param)
if result != params.SUCCESS &#123;

  // Non-json mode also can not be returned in this way, you need to call the Send function in the res object to return the result to the front end
  res.SendErrorMsg(500, result)
  return
&#125;</code></pre> 
 <p>现在改成了这样，只需要传指针</p> 
 <pre><code class="language-go">var result = params.Validation(req, &param)
if result != params.SUCCESS &#123;

  // Non-json mode also can not be returned in this way, you need to call the Send function in the res object to return the result to the front end
  res.SendErrorMsg(500, result)
  return
&#125;</code></pre> 
 <h2>感兴趣的伙伴们可以访问官网查看更多哦</h2> 
 <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbeeruscc.com%2F" target="_blank">https://beeruscc.com</a></p> 
</div>
                                        </div>
                                      
</div>
            