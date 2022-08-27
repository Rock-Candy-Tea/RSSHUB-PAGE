
---
title: '一站式 Go 开发框架 Go-Spring 正式发布 v1.1.1 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6367'
author: 开源中国
comments: false
date: Sat, 27 Aug 2022 11:10:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6367'
---

<div>   
<div class="content">
                                                                                            <p>在经历了一年半的折腾后，go-spring v1.1.1 终于发布了，这是一个全面重构的版本，更加符合 go 语言的开发习惯。</p> 
<ul> 
 <li>它是一个全新的版本，命名更加符合 go 规范，模块划分更加合理，核心设计也更加简洁；</li> 
 <li>它是一个具有重大突破的版本，突破性的支持统一日志框架，突破性的支持流量录制和回放；</li> 
 <li>它是一个功能庞大的版本，涵盖了日常开发所需的方方面面，再也不用纠结使用哪个依赖包。</li> 
</ul> 
<p>1. 新版本 log 模块全面遵循 log4j2 的架构，具有超级灵活的适配能力。</p> 
<blockquote> 
 <p>func init() &#123;<br>     log.RegisterPlugin("ExampleLayout", log.PluginTypeLayout, (*ExampleLayout)(nil))<br> &#125;</p> 
 <p>type ExampleLayout struct &#123;<br>     LineBreak bool `PluginAttribute:"lineBreak,default=true"`<br> &#125;</p> 
 <p>func (c *ExampleLayout) ToBytes(e *log.Event) ([]byte, error) &#123;<br>     buf := bytes.NewBuffer(nil)<br>     enc := log.NewFlatEncoder(buf, "||")<br>     prefix := fmt.Sprintf("[%s][%s:%d][%s] ", e.Level(), e.File(), e.Level(), e.Time().Format("2006-01-02 15:04:05.000"))<br>     err := enc.AppendBuffer([]byte(prefix))<br>     if err != nil &#123;<br>         return nil, err<br>     &#125;<br>     if ctx := e.Entry().Context(); ctx != nil &#123;<br>         span := SpanFromContext(ctx)<br>         if span != nil &#123;<br>             s := fmt.Sprintf("trace_id=%s||span_id=%s||", span.TraceID, span.SpanID)<br>             err = enc.AppendBuffer([]byte(s))<br>             if err != nil &#123;<br>                 return nil, err<br>             &#125;<br>         &#125;<br>     &#125;<br>     for _, f := range e.Fields() &#123;<br>         err = enc.AppendKey(f.Key)<br>         if err != nil &#123;<br>             return nil, err<br>         &#125;<br>         err = f.Val.Encode(enc)<br>         if err != nil &#123;<br>             return nil, err<br>         &#125;<br>     &#125;<br>     if c.LineBreak &#123;<br>         buf.WriteByte('\n')<br>     &#125;<br>     return buf.Bytes(), nil<br> &#125;</p> 
 <p>func main() &#123;</p> 
 <p>    config := `<br>         <?xml version="1.0" encoding="UTF-8"?><br>         <Configuration><br>             <Appenders><br>                 <Console name="Console"><br>                     <ExampleLayout/><br>                 </Console><br>             </Appenders><br>             <Loggers><br>                 <Root level="trace"><br>                     <AppenderRef ref="Console"/><br>                 </Root><br>             </Loggers><br>         </Configuration><br>     `</p> 
 <p>    err := log.RefreshBuffer(config, ".xml")<br>     util.Panic(err).When(err != nil)</p> 
 <p>    logger := log.GetLogger("xxx")<br>     logger.Info("a", "=", "1")<br>     logger.Infof("a=1")<br>     logger.Infow(log.Message("a=%d", 1))</p> 
 <p>    span := &Span&#123;TraceID: "1111", SpanID: "2222"&#125;<br>     ctx := ContextWithSpan(context.Background(), span)<br>     logger.WithContext(ctx).Info("a", "=", "1")<br>     logger.WithContext(ctx).Infof("a=1")<br>     logger.WithContext(ctx).Infow(log.Message("a=%d", 1))<br> &#125;</p> 
 <p>///////////////////////////// observability /////////////////////////////</p> 
 <p>type Span struct &#123;<br>     TraceID string<br>     SpanID  string<br> &#125;</p> 
 <p>type spanKeyType int</p> 
 <p>var spanKey spanKeyType</p> 
 <p>func SpanFromContext(ctx context.Context) *Span &#123;<br>     v := ctx.Value(spanKey)<br>     if v == nil &#123;<br>         return nil<br>     &#125;<br>     return v.(*Span)<br> &#125;</p> 
 <p>func ContextWithSpan(ctx context.Context, span *Span) context.Context &#123;<br>     return context.WithValue(ctx, spanKey, span)<br> &#125;</p> 
</blockquote> 
<p>2. 新版本 IoC 容器支持 Logger 注入，日常开发非常方便，同时支持结构化日志。</p> 
<blockquote> 
 <p>type MyController struct &#123;<br>     Logger      *log.Logger   `logger:""`<br> &#125;</p> 
 <p>func (c *MyController) onInit(ctx gs.Context) error &#123;<br>     ctx.Go(func(ctx context.Context) &#123;<br>         defer func() &#123; c.Logger.Info("exit after waiting in ::Go") &#125;()</p> 
 <p>        ticker := time.NewTicker(10 * time.Millisecond)<br>         defer ticker.Stop()</p> 
 <p>        for &#123;<br>             select &#123;<br>             case <-ctx.Done():<br>                 return<br>             case <-ticker.C:<br>                 c.Logger.Info("::Go")<br>             &#125;<br>         &#125;<br>     &#125;)<br>     return nil<br> &#125;</p> 
</blockquote> 
<p>3. 新版本支持完全不使用 Go-Spring 内置的启动架构，只使用 IoC 容器也能启动 Web 服务。</p> 
<blockquote> 
 <p>package main</p> 
 <p>import (<br>     "fmt"<br>     "net/http"</p> 
 <p>    "github.com/gin-gonic/gin"<br>     "github.com/go-spring/spring-base/log"<br>     "github.com/go-spring/spring-base/util"<br>     "github.com/go-spring/spring-core/gs"<br> )</p> 
 <p>//---------------- Controller -----------------------------//</p> 
 <p>type Controller struct &#123;<br>     HelloController<br> &#125;</p> 
 <p>type HelloController struct &#123;<br>     Service *HelloService `autowire:""`<br> &#125;</p> 
 <p>func (c *HelloController) Hello(ctx *gin.Context) &#123;<br>     s := c.Service.Hello(ctx.Query("name"))<br>     ctx.String(http.StatusOK, s)<br> &#125;</p> 
 <p>//---------------- Service -------------------------------//</p> 
 <p>type HelloService struct &#123;<br> &#125;</p> 
 <p>func (s *HelloService) Hello(name string) string &#123;<br>     return "hello " + name + "!"<br> &#125;</p> 
 <p>//---------------- Engine --------------------------------//</p> 
 <p>type Engine struct &#123;<br>     Engine     *gin.Engine<br>     Address    string        `value:"$&#123;http.addr:=:8080&#125;"`<br>     Controller *Controller   `autowire:""`<br>     Exit       chan struct&#123;&#125; `autowire:""`<br> &#125;</p> 
 <p>func (e *Engine) Init() &#123;<br>     e.Engine = gin.Default()<br>     e.Engine.GET("/hello", e.Controller.Hello)<br>     go func() &#123;<br>         err := e.Engine.Run(e.Address)<br>         fmt.Println(err)<br>         e.Exit <- struct&#123;&#125;&#123;&#125;<br>     &#125;()<br> &#125;</p> 
 <p>//---------------- main ---------------------------------//</p> 
 <p>func main() &#123;</p> 
 <p>    config := `<br>         <?xml version="1.0" encoding="UTF-8"?><br>         <Configuration><br>             <Appenders><br>                 <Console name="Console"/><br>             </Appenders><br>             <Loggers><br>                 <Root level="info"><br>                     <AppenderRef ref="Console"/><br>                 </Root><br>             </Loggers><br>         </Configuration><br>     `<br>     err := log.RefreshBuffer(config, ".xml")<br>     util.Panic(err).When(err != nil)</p> 
 <p>    exit := make(chan struct&#123;&#125;)<br>     c := gs.New()<br>     c.Object(exit)<br>     c.Object(new(Controller))<br>     c.Object(new(HelloService))<br>     c.Object(new(Engine)).Init((*Engine).Init)<br>     err = c.Refresh()<br>     util.Panic(err).When(err != nil)<br>     <-exit<br>     c.Close()<br> &#125;</p> 
</blockquote>
                                        </div>
                                      
</div>
            