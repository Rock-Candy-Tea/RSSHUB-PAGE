
---
title: '如何在 Filebeat 端进行日志处理'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210821/efe5df5df2cc4219e334de8a735c1b27.jpeg'
author: Dockone
comments: false
date: 2021-08-22 10:07:43
thumbnail: 'https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210821/efe5df5df2cc4219e334de8a735c1b27.jpeg'
---

<div>   
<br><h3>一、起因</h3>目前某项目组日志需要做切割处理，针对日志信息进行分割并提取 K/V 放入 ES 中方便查询。这种需求在传统 ELK 中应当由 Logstash 组件完成，通过 <code class="prettyprint">gork</code> 等操作对日志进行过滤、切割等处理。不过很尴尬的是我并不会 Ruby，Logstash Pipeline 的一些配置我也是极其头疼，而且还不想学……更不凑巧的是我会写点 Go，那么理所应当的此时的我对 Filebeat 源码产生了一些想法，比如我直接在 Filebeat 端完成日志处理，然后直接发 ES/Logstash，这样似乎更方便，而且还能分摊 Logstash 的压力，我感觉这个操作并不过分……<br>
<h3>二、需求</h3>目前某项目组 Java 日志格式如下：<br>
<pre class="prettyprint">2020-04-30 21:56:30.117$$api-test-65c8c7cf7f-lng7h$$http-nio-8080-exec-3$$INFO$$com.example.api.common.filter.GlobalDataFilter$$GlobalDataFilter.java$$95$$test<br>
build commonData from header :&#123;"romVersion":"W_V2.1.4","softwareVersion":"15","token":"aFxANNM3pnRYpohvLMSmENydgFSfsmFMgCbFWAosIE="&#125;<br>
$$$$<br>
</pre><br>
目前开发约定格式为日志通过 <code class="prettyprint">$$</code> 进行分割，日志格式比较简单，但是 Logstash 共用（Nginx 等各种日志都会往这个 Logstash 输出），不想去折腾 Logstash 配置的情况下，只需要让 Filebeat 能够直接切割并设置好 K/V 对应既可。<br>
<h3>三、Filebeat Module</h3><em>Module 部份只做简介，以为实际上依托 ES 完成，意义不大</em>。<br>
<br>当然在考虑修改 Filebeat 源码后，我第一想到的是 Filebeat 的 module，这个 module 在官方文档中是个很神奇的东西；通过开启一个 module 就可以对某种日志直接做处理，这种东西似乎就是我想要的；比如我写一个 “项目名” module，然后 Filebeat 直接开启这个 module，这个项目的日志就直接自动处理好（听起来就很 “上流”）……<br>
<br>针对于自定义 module，官方给出了文档：<a href="https://www.elastic.co/guide/en/beats/devguide/current/filebeat-modules-devguide.html">Creating a New Filebeat Module</a><br>
<br>按照文档操作如下（假设我们的项目名为 cdm）：<br>
<pre class="prettyprint"># 克隆源码<br>
git clone git@github.com:elastic/beats.git<br>
# 切换到稳定分支<br>
cd bests && git checkout -b v7.6.2 v7.6.2-module<br>
# 创建 module，GO111MODULE 需要设置为 off<br>
# 在 7.6.2 版本官方尚未开始支持 go mod<br>
cd filebeat<br>
GO111MODULE=off make create-module MODULE=cdm<br>
</pre><br>
创建完成后目录结构如下：<br>
<pre class="prettyprint">➜  filebeat git:(v7.6.2-module) ✗ tree module/cdm<br>
module/cdm<br>
├── _meta<br>
│   ├── config.yml<br>
│   ├── docs.asciidoc<br>
│   └── fields.yml<br>
└── module.yml<br>
<br>
1 directory, 4 files<br>
</pre><br>
这几个文件具体作用<a href="https://www.elastic.co/guide/en/beats/devguide/current/filebeat-modules-devguide.html">官方文档</a>都有详细的描述；但是根据文档描述光有这几个文件是不够的，module 只是一个处理集合的定义，尚未包含任何处理，针对真正的处理需要继续创建 Fileset，Fileset 简单的理解就是针对具体的一组文件集合的处理；例如官方 Nginx module 中包含两个 fileset：<code class="prettyprint">access</code> 和 <code class="prettyprint">error</code>，这两个一个针对 access 日志处理一个针对 error 日志进行处理；在 fileset 中可以设置默认文件位置、处理方式。<br>
<br>But……我翻了 Nginx module 的样例配置才发现，module 这个东西实质上只做定义和存储处理表达式，具体的切割处理实际上交由 ES 的 <a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest.html">Ingest Node</a> 处理；表达式里仍需要定义 <code class="prettyprint">grok</code> 等操作，而且这东西最终会编译到 Go 静态文件里；此时的我想说一句 “MMP”，本来我是不想写 grok 啥的才来折腾 Filebeat，结果这个 module 折腾一圈还是要写 grok 啥的，而且这东西直接借助 ES 完成导致压力回到了 ES 同时每次修改还得重新编译 Filebeat……所以折腾到这我就放弃了，这已经违背了当初的目的，有兴趣的可以参考以下文档继续折腾：<br>
<ul><li><a href="https://www.elastic.co/guide/en/beats/devguide/current/filebeat-modules-devguide.html">Creating a New Filebeat Module</a></li><li><a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest.html">Ingest nodeedit</a></li><li><a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest-apis.html">Ingest APIs</a></li><li><a href="https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest-processors.html">Processors</a></li></ul><br>
<br><h3>四、Filebeat processors</h3>经历了 module 的失望以后，我把目光对准了 processors；processors 是 Filebeat 一个强大的功能，顾名思义它可以对 Filbeat 收集到的日志进行一些处理；从官方 <a href="https://www.elastic.co/guide/en/beats/filebeat/current/filtering-and-enhancing-data.html">Processors</a> 页面可以看到其内置了大量的 processor；这些 processor 大部份都是直接对日志进行 “写” 操作，所以理论上我们自己写一个 processor 就可以 “为所欲为+为所欲为=为所欲为”。<br>
<br>不过不幸的是关于 processor 的开发官方并未给出文档，官方认为这是一个 <code class="prettyprint">high level</code> 的东西，不过也找到了一个 issue 对其做了相关回答：<a href="https://github.com/elastic/beats/issues/6760">How do I write a processor plugin by myself</a>；所以最好的办法就是直接看已有 processor 的源码抄一个。<br>
<br>理所应当的找了一个软柿子捏：<code class="prettyprint">add_host_metadata</code>，add_host_metadata processor 顾名思义在每个日志事件（以下简称为 event）中加入宿主机的信息，比如 hostname 啥的；以下为 add_host_metadata processor 的文件结构（processors 代码存储在 <code class="prettyprint">libbeat/processors</code> 目录下）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210821/efe5df5df2cc4219e334de8a735c1b27.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210821/efe5df5df2cc4219e334de8a735c1b27.jpeg" class="img-polaroid" title="1.jpeg" alt="1.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>dir_tree</em><br>
<br>通过阅读源码和 issue 的回答可以看出，我们自定义的 processor 只需要实现 <a href="https://godoc.org/github.com/elastic/beats/libbeat/processors#Processor">Processor interface</a> 既可，这个接口定义如下：<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210821/e7ff9f2e15f2ec4c56de4f34512e2a15.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210821/e7ff9f2e15f2ec4c56de4f34512e2a15.png" class="img-polaroid" title="2.png" alt="2.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Processor interface</em><br>
<br>通过查看 add_host_metadata 的源码，<code class="prettyprint">String() string</code> 方法只需要返回这个 processor 名称既可（可以包含必要的配置信息）；而 <code class="prettyprint">Run(event *beat.Event) (*beat.Event, error)</code> 方法表示在每一条日志被读取后都会转换为一个 event 对象，我们在方法内进行处理然后把 event 返回既可（其他 processor 可能也要处理）。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210821/80c91e273fd0d27d1f9ca3d75863f519.png" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210821/80c91e273fd0d27d1f9ca3d75863f519.png" class="img-polaroid" title="3.png" alt="3.png" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>add_host_metadata source</em><br>
<br>有了这些信息就简单得多了，毕竟作为一名合格的 CCE（Ctrl C + Ctrl V + Engineer）抄这种操作还是很简单的，直接照猫画虎写一个就行了。<br>
<br>config.go<br>
<pre class="prettyprint">package cmd<br>
<br>
// Config for cdm processor.<br>
type Config struct &#123;<br>
Name           string          `config:"name"`<br>
&#125;<br>
<br>
func defaultConfig() Config &#123;<br>
return Config&#123;<br>
&#125;<br>
&#125; <br>
</pre><br>
cdm.go<br>
<pre class="prettyprint">package cmd<br>
<br>
import (<br>
"strings"<br>
<br>
"github.com/elastic/beats/libbeat/logp"<br>
"github.com/pkg/errors"<br>
<br>
"github.com/elastic/beats/libbeat/beat"<br>
"github.com/elastic/beats/libbeat/common"<br>
"github.com/elastic/beats/libbeat/processors"<br>
jsprocessor "github.com/elastic/beats/libbeat/processors/script/javascript/module/processor"<br>
)<br>
<br>
func init() &#123;<br>
processors.RegisterPlugin("cdm", New)<br>
jsprocessor.RegisterPlugin("CDM", New)<br>
&#125;<br>
<br>
type cdm struct &#123;<br>
config Config<br>
fields []string<br>
log    *logp.Logger<br>
&#125;<br>
<br>
const (<br>
processorName = "cdm"<br>
logName       = "processor.cdm"<br>
)<br>
<br>
// New constructs a new cdm processor.<br>
func New(cfg *common.Config) (processors.Processor, error) &#123;<br>
// 配置文件里就一个 Name 字段，结构体留着以后方便扩展<br>
config := defaultConfig()<br>
if err := cfg.Unpack(&config); err != nil &#123;<br>
    return nil, errors.Wrapf(err, "fail to unpack the %v configuration", processorName)<br>
&#125;<br>
<br>
p := &cdm&#123;<br>
    config: config,<br>
    // 待分割的每段日志对应的 key<br>
    fields: []string&#123;"timestamp", "hostname", "thread", "level", "logger", "file", "line", "serviceName", "traceId", "feTraceId", "msg", "exception"&#125;,<br>
    log:    logp.NewLogger(logName),<br>
&#125;<br>
<br>
return p, nil<br>
&#125;<br>
<br>
// 真正的日志处理逻辑<br>
// 为了保证后面的 processor 正常处理，这里面没有 return 任何 error，只是简单的打印<br>
func (p *cdm) Run(event *beat.Event) (*beat.Event, error) &#123;<br>
// 尝试获取 message，理论上这一步不应该出现问题<br>
msg, err := event.GetValue("message")<br>
if err != nil &#123;<br>
    p.log.Error(err)<br>
    return event, nil<br>
&#125;<br>
<br>
message, ok := msg.(string)<br>
if !ok &#123;<br>
    p.log.Error("failed to parse message")<br>
    return event, nil<br>
&#125;<br>
<br>
// 分割日志<br>
fieldsValue := strings.Split(message, "$$")<br>
p.log.Debugf("message fields: %v", fieldsVaule)<br>
// 为了保证不会出现数组越界需要判断一下（万一弄出个格式不正常的日志过来保证不崩）<br>
if len(fieldsValue) < len(p.fields) &#123;<br>
    p.log.Errorf("incorrect field length: %d, expected length: %d", len(fieldsValue), len(p.fields))<br>
    return event, nil<br>
&#125;<br>
<br>
// 这里遍历然后赛会到 event 既可<br>
data := common.MapStr&#123;&#125;<br>
for i, k := range p.fields &#123;<br>
    _, _ = event.PutValue(k, strings.TrimSpace(fieldsValue[i]))<br>
&#125;<br>
event.Fields.DeepUpdate(data)<br>
<br>
return event, nil<br>
&#125;<br>
<br>
func (p *cdm) String() string &#123;<br>
return processorName<br>
&#125; <br>
</pre><br>
写好代码以后就可以编译一个自己的 Filebeat 了（开心ing）。<br>
<pre class="prettyprint">cd filebeat<br>
# 如果想交叉编译 linux 需要增加 GOOS=linux 变量 <br>
GO111MODULE=off make<br>
</pre><br>
然后编写配置文件进行测试，日志相关字段已经成功塞到了 event 中，这样我直接发到 ES 或者 Logstash 就行了。<br>
<pre class="prettyprint">filebeat.inputs:<br>
- type: log<br>
enabled: true<br>
paths:<br>
- /Users/natural/tmp/cdm.log<br>
processors:<br>
- cdm: ~<br>
multiline.pattern: ^\d&#123;4&#125;-\d&#123;1,2&#125;-\d&#123;1,2&#125;<br>
multiline.match: after<br>
multiline.negate: true<br>
multiline.timeout: 5s<br>
</pre><br>
<h3>五、Script Processor</h3>在我折腾完源码以后，反思一下其实这种方式需要自己编译 Filebeat，而且每次规则修改也很不方便，唯一的好处真的就是用代码可以 “为所欲为”；反过来一想 “Filebeat 有没有 processor 的扩展呢？脚本热加载那种？” 答案是使用 Script Processor，<strong>Script Processor 虽然名字上是个 processor，实际上其包含了完整的 ECMA 5.1 js 规范实现；结论就是我们可以写一些 js 脚本来处理日志，然后 Filebeat 每次启动后加载这些脚本既可</strong>。<br>
<br>Script Processor 的使用方式很简单，js 文件中只需要包含一个 <code class="prettyprint">function process(event)</code> 方法既可，与自己用 Go 实现的 processor 类似，每行日志也会形成一个 event 对象然后调用这个方法进行处理；目前 event 对象可用的 API 需要参考<a href="https://www.elastic.co/guide/en/beats/filebeat/current/processor-script.html#_event_api">官方文档</a>；<strong>需要注意的是 Script Processor 目前只支持 ECMA 5.1 语法规范，超过这个范围的语法是不被支持</strong>；实际上其根本是借助了 <a href="https://github.com/dop251/goja"></a><a href="https://github.com/dop251/goja" rel="nofollow" target="_blank">https://github.com/dop251/goja</a>  这个库来实现的。同时为了方便开发调试，Script Processor 也增加了一些 nodejs 的兼容 module，比如 <code class="prettyprint">console.log</code> 等方法是可用的；以下为 js 处理上面日志的逻辑：<br>
<pre class="prettyprint">var console = require('console');<br>
var fileds = new Array("timestamp", "hostname", "thread", "level", "logger", "file", "line", "serviceName", "traceId", "feTraceId", "msg", "exception")<br>
<br>
function process(event) &#123;<br>
var message = event.Get("message");<br>
if (message == null || message == undefined || message == '') &#123;<br>
    console.log("failed to get message");<br>
    return<br>
&#125;<br>
var fieldValues = message.split("$$");<br>
if (fieldValues.length<fileds.length) &#123;<br>
    console.log("incorrect field length");<br>
    return<br>
&#125;<br>
for (var i = 0; i < fileds.length; ++i) &#123;<br>
    event.Put(fileds[i],fieldValues[i].trim())<br>
&#125;<br>
&#125; <br>
</pre><br>
写好脚本后调整配置测试既可，如果 js 编写有问题，可以通过 <code class="prettyprint">console.log</code> 来打印日志进行不断的调试。<br>
<pre class="prettyprint">filebeat.inputs:<br>
- type: log<br>
enabled: true<br>
paths:<br>
- /Users/natural/tmp/cdm.log<br>
processors:<br>
- script:<br>
    lang: js<br>
    id: cdm<br>
    file: cdm.js<br>
multiline.pattern: ^\d&#123;4&#125;-\d&#123;1,2&#125;-\d&#123;1,2&#125;<br>
multiline.match: after<br>
multiline.negate: true<br>
multiline.timeout: 5s<br>
</pre><br>
需要注意的是目前 <code class="prettyprint">lang</code> 的值只能为 <code class="prettyprint">JavaScript</code> 和 <code class="prettyprint">js</code>（官方文档写的只能是  <code class="prettyprint">JavaScript</code>）；根据代码来看后续 Script Processor 有可能支持其他脚本语言，个人认为主要取决于其他脚本语言有没有纯 Go 实现的 runtime，如果有的话未来很有可能被整合到 Script Processor 中。<br>
<div class="aw-upload-img-list active">
<a href="http://dockone.io/uploads/article/20210821/0d65885912b120a5779d8e326ef4c92c.jpeg" target="_blank" data-fancybox-group="thumb" rel="lightbox"><img src="https://cors.zfour.workers.dev/?http://dockone.io/uploads/article/20210821/0d65885912b120a5779d8e326ef4c92c.jpeg" class="img-polaroid" title="4.jpeg" alt="4.jpeg" referrerpolicy="no-referrer"></a>
</div>
<br>
<em>Script Processor</em><br>
<h3>六、其他 processor</h3>研究完 Script Processor 后我顿时对其他 processor 也产生了兴趣，随着更多的查看 processor 文档，我发现其实大部份过滤分割能力已经有很多 processor 进行了实现，<strong>其完善程度外加可扩展的 Script Processor 实际能力已经足矣替换掉 Logstash 的日志分割过滤处理了。</strong>比如上面的日志切割其实使用 dissect processor 实现更加简单（这个配置并不完善，只是样例）：<br>
<pre class="prettyprint">processors:<br>
- dissect:<br>
  field: "message"<br>
  tokenizer: "%&#123;timestamp&#125;$$%&#123;hostname&#125;$$%&#123;thread&#125;$$%&#123;level&#125;$$%&#123;logger&#125;$$%&#123;file&#125;$$%&#123;line&#125;$$%&#123;serviceName&#125;$$%&#123;traceId&#125;$$%&#123;feTraceId&#125;$$%&#123;msg&#125;$$%&#123;exception&#125;$$"<br>
</pre><br>
除此之外还有很多 processor，例如 <code class="prettyprint">drop_event</code>、<code class="prettyprint">drop_fields</code>、<code class="prettyprint">timestamp</code> 等等，感兴趣的可以自行研究。<br>
<h3>七、总结</h3>基本上折腾完以后做了一个总结：<br>
<ul><li><strong>Filebeat module</strong>：这就是个华而不实的东西，每次修改需要重新编译且扩展能力几近于零，最蛋疼的是实际逻辑通过 ES 来完成；我能想到的是唯一应用场景就是官方给我们弄一些 demo 来炫耀用的，比如 Nginx module；实际生产中 Nginx 日志格式保持原封不动的人我相信少之又少。</li><li><strong>Filebeat custom processor</strong>：每次修改也需要重新编译且需要会 Go 语言还有相关工具链，但是好处就是完全通过代码实现真正的为所欲为；扩展性取决于外部是否对特定位置做了可配置化，比如预留可以配置切割用正则表达式的变量等，最终取决于代码编写者（怎么为所欲为的问题）。</li><li><strong>Filebeat Script Processor</strong>：完整 ECMA 5.1 js 规范支持，代码化对日志进行为所欲为，修改不需要重新编译；普通用户我个人觉得是首选，当然同时会写 Go 和 js 的就看你想用哪个了。</li><li><strong>Filebeat other processor</strong>：基本上实现了很多 Logstash 的功能，简单用用很舒服，复杂场景还是得撸代码；但是一些特定的 processor 很实用，比如加入宿主机信息的 add_host_metadata processor 等。</li></ul><br>
<br>原文链接：22020/08/19/how-to-modify-filebeat-source-code-to-processing-logs/，作者：bleem
                                                                <div class="aw-upload-img-list">
                                                                                                                                                                                                                                                                                                                                </div>
                                
                                                                <ul class="aw-upload-file-list">
                                                                                                                                                                                                                                                                                                                                                                    </ul>
                                                              
</div>
            