
---
title: 'Beerus 上线啦，用 Go 开发的 web 解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5817'
author: 开源中国
comments: false
date: Mon, 13 Dec 2021 22:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5817'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Beerus是一个用 Go 开发的 web 解决方案，包含一个 web 框架，一个数据库操作框架，一个正在规划中的RPC框架，目前 web 框架和数据库操作框架已经发布了第一个版本。</p> 
<h2>Web框架</h2> 
<p>因为他是牵头的框架，说到web大家想到的肯定是接口管理，所以他的名字就直接沿用了Beerus，也就是这一套项目的品牌名称，它是<span style="background-color:#ffffff">以net/http 为基础，在此基础上扩展了路由的管理方式，并增加了拦截器，会话管理，用struct接收参数，参数验证等功能，还提供了WebSocket支持，可以将http协议升级到WebSocket 并实现通信</span></p> 
<h2><span style="background-color:#ffffff">数据库操作框架</span></h2> 
<p><span style="background-color:#ffffff">名字叫Beerus-DB，</span><span style="background-color:#ffffff">用到了[go-sql-driver/mysql]来做数据库连接与基础操作，在此基础上做了很多扩展，比如：连接池管理，多数据源，事务管理，单表无sql操作，多表以及复杂操作可以自己写sql，sql支持&#123;&#125;占位符，可以用struct作为参数来操作数据库等</span></p> 
<h2>示例</h2> 
<h3><span>​</span>HTTP 示例</h3> 
<p style="color:#24292f; text-align:start">创建一个函数管理路由</p> 
<div style="text-align:start"> 
 <pre><code class="language-go">func CreateRoute() &#123;
// post route example
    route.POST("/example/post", func (req *commons.BeeRequest, res *commons.BeeResponse) &#123;
        
        res.SendJson(`&#123;"msg":"SUCCESS"&#125;`)
    &#125;)

    // get route example
    route.GET("/example/get", func (req *commons.BeeRequest, res *commons.BeeResponse) &#123;
    
        res.SendJson(`&#123;"msg":"SUCCESS"&#125;`)
    &#125;)
&#125;</code></pre> 
 <p>启动服务</p> 
</div> 
<div style="text-align:start"> 
 <pre><code class="language-go">func main() &#123;
    // Interceptors, routes, etc. Loading of data requires its own calls
    routes.CreateRoute()
    
    // Listen the service and listen to port 8080
    beerus.ListenHTTP(8080)
&#125;</code></pre> 
 <p>如果你想用实体接收参数，可以这么做</p> 
</div> 
<div style="text-align:start"> 
 <pre><code class="language-go">func CreateRoute() &#123;
    // Example of parameter conversion to struct and parameter checksum
    route.POST("/example/post", func (req *commons.BeeRequest, res *commons.BeeResponse) &#123;
        
        // 首先需要建一个实体的实例
        param := DemoParam&#123;&#125;
        
        // 调用这个函数，将请求的参数全部提取到实体中，支持任意请求方式
        params.ToStruct(req, &param, param)
        
        // 对参数进行验证，如果没通过就返回 提示信息
        var result = params.Validation(req, &param, param)
        if result != params.SUCCESS &#123;
            res.SendErrorMsg(1128, result)
            return
        &#125;
        
        // 如果你觉得上面的麻烦，那么也可以这样，直接采用一步到位的方式：参数提取 + 验证
        var result = params.ToStructAndValidation(req, &param, param)
        if result != params.SUCCESS &#123;
            res.SendErrorMsg(1128, result)
            return
        &#125;
        
        
        res.SendJson(`&#123;"msg":"SUCCESS"&#125;`)
    &#125;)
&#125;

// DemoParam If you have a struct like this, and you want to put all the parameters from the request into this struct
type DemoParam struct &#123;
    TestStringReception  string  `notnull:"true" msg:"TestStringReception Cannot be empty" routes:"/example/put"`
    TestIntReception     int     `max:"123" min:"32" msg:"TestIntReception The value range must be between 32 - 123" routes:"/example/post"`
    TestUintReception    uint    `max:"123" min:"32" msg:"TestUintReception The value range must be between 32 - 123"`
    TestFloatReception   float32 `max:"123" min:"32" msg:"TestFloatReception The value range must be between 32 - 123"`
    TestBoolReception    bool
    TestStringRegReception string `reg:"^[a-z]+$" msg:"TestStringRegReception Does not meet the regular"`
    TestBeeFileReception commons.BeeFile
    
    TestJsonReception []string
&#125;</code></pre> 
 <h3>WebSocket 示例</h3> 
</div> 
<p style="color:#24292f; text-align:start">创建一个函数来管理WebSocket路由</p> 
<div style="text-align:start"> 
 <pre><code class="language-go">func CreateWebSocketRoute() &#123;
wroute.AddWebSocketRoute("/ws/test", onConnection, onMessage, onClose)
wroute.AddWebSocketRoute("/ws/test2", onConnection, onMessage, onClose)
&#125;

// In order to save time, only three functions are used below. In practice, you can configure a set of functions for each wroute

func onConnection(session *wparams.WebSocketSession, msg string) &#123;
session.SendString("connection success")
&#125;

func onMessage(session *wparams.WebSocketSession, msg string) &#123;
session.SendString("I got the message.")
&#125;

func onClose(session *wparams.WebSocketSession, msg string) &#123;
    println(msg + "-------------------------------")
&#125;</code></pre> 
 <p>启动服务</p> 
</div> 
<div style="text-align:start"> 
 <pre><code class="language-go">func main() &#123;
    // Interceptors, routes, etc. Loading of data requires its own calls
    routes.CreateRoute()
    routes.CreateWebSocketRoute()
    
    // Listen the service and listen to port 8080
    beerus.ListenHTTP(8080)
&#125;</code></pre> 
 <h3><span>​</span>单表操作</h3> 
</div> 
<p style="text-align:start">根据条件查询单表数据</p> 
<pre><code class="language-go">conditions := make([]*entity.Condition,0)
conditions = append(conditions, &entity.Condition&#123;Key:"id > ?", Val: 10&#125;)
conditions = append(conditions, &entity.Condition&#123;Key:"and user_name = ?", Val: "bee"&#125;)
conditions = append(conditions, &entity.Condition&#123;Key: "order by create_time desc", Val: entity.NotWhere&#125;)

resultMap, err := operation.GetDBTemplate("Data source name").Select("table name", conditions)</code></pre> 
<p style="text-align:start">根据条件修改单表数据</p> 
<pre><code class="language-go">// 条件设定
conditions := make([]*entity.Condition,0)
conditions = append(conditions, &entity.Condition&#123;Key:"id = ?", Val: 1&#125;)

// 要修改的数据设定
data := ResultStruct&#123;UserName: "TestNoSqlUpdate"&#125;

// 执行修改操作
result, err := operation.GetDBTemplate("Data source name").Update("table name", dbutil.StructToMapIgnore(&data, data, true),conditions)</code></pre> 
<p style="text-align:start">根据条件删除单表数据</p> 
<pre><code class="language-go">// 设定删除条件
conditions := make([]*entity.Condition,0)
conditions = append(conditions, &entity.Condition&#123;Key:"id = ?", Val: 2&#125;)

// 执行删除操作
_, err := operation.GetDBTemplate("Data source name").Delete("table name", conditions)</code></pre> 
<p style="text-align:start">插入一条数据</p> 
<pre><code class="language-go">data := ResultStruct&#123;
    UserName: "TestNoSqlInsert",
    UserEmail: "xxxxx@163.com",
    UpdateTime: "2021-12-09 13:50:00",
&#125;

result, err := operation.GetDBTemplate("Data source name").Insert("table name", dbutil.StructToMapIgnore(&data, data, true))</code></pre> 
<h2>自定义sql</h2> 
<p>查询</p> 
<pre><code class="language-go">// struct参数
res := ResultStruct&#123;Id: 1&#125;

// 查多条, 注：这里需要用到占位符
resultMap, err := operation.GetDBTemplate("Data source name").SelectListByMap("select * from xt_message_board where id < &#123;id&#125;", dbutil.StructToMap(&res, res))

// 查一条, 注：这里需要用到占位符
resultMap, err := operation.GetDBTemplate("Data source name").SelectOneByMap("select * from xt_message_board where id < &#123;id&#125;", dbutil.StructToMap(&res, res))</code></pre> 
<p>增删改</p> 
<pre><code class="language-go">res := ResultStruct&#123;Id: 1, UserName: "TestUpdateByMap"&#125;

// 无论是增删改，都是调用ExecByMap函数，将sql和参数传入即可，注：这里需要用到占位符
operation.GetDBTemplate("Data source name").ExecByMap("update xt_message_board set user_name = &#123;user_name&#125; where id = &#123;id&#125;", dbutil.StructToMap(&res, res))</code></pre> 
<h2>分页查询</h2> 
<pre><code class="language-go">data := ResultStruct&#123;
    UserName: "TestNoSqlInsert",
    UserEmail: "xxxxx@163.com",
&#125;

// 创建分页参数
param := entity.PageParam&#123;
    CurrentPage: 1,  // 第几页
    PageSize: 20,  // 每页多少条
    Params: dbutil.StructToMap(&data, data)， // 查询参数
&#125;

// 执行查询操作
result, err := operation.GetDBTemplate("Data source name").SelectPage("select * from xt_message_board where user_name = &#123;user_name&#125; and user_email = &#123;user_email&#125;", param)</code></pre> 
<h2>事务管理</h2> 
<pre><code class="language-go">// 开启事务
id, err := db.Transaction()
if err != nil &#123;
    t.Error("TestUpdateTx: " + err.Error())
    return
&#125;

res := ResultStruct&#123;Id: 1, UserName: "TestUpdateTx"&#125;

// 注：这里使用的不是GetDBTemplate，ExecByMap，而是 GetDBTemplateTx 和 ExecByTxMap
// 使用事务和不使用事务，在调用的函数上，区别就是多了个Tx
ss, err := operation.GetDBTemplateTx(id, "dbPoolTest").ExecByTxMap("update xt_message_board set user_name = &#123;user_name&#125; where id = &#123;id&#125;", dbutil.StructToMap(&res, res))

if err != nil &#123;
    // 如果有问题就回滚事务
    db.Rollback(id)
    t.Error("TestUpdateTx: " + err.Error())
    return
&#125;

// 提交事务
db.Commit(id)</code></pre> 
<p>想了解更多的话，可以查阅我们的文档哦</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbeeruscc.com" target="_blank">https://beeruscc.com</a></p>
                                        </div>
                                      
</div>
            