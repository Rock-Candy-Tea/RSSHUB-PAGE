
---
title: '一站式开发框架 Go-Spring 发布 v1.1.2 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8658'
author: 开源中国
comments: false
date: Tue, 13 Sep 2022 13:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8658'
---

<div>   
<div class="content">
                                                                                            <p>距离上次发版仅两周的时间，Go 后端一站式开发框架 Go-Spring 又发布了新的版本，新版本实现了两个非常重要的特性：动态配置和 Bean 共享。</p> 
<p><strong>动态配置</strong></p> 
<p>有时候我们想要在不停机的情况下可以修改程序的配置，更改程序的行为，即所谓的“动态配置”。Go-Spring 通过使用专门的数据类型实现了和普通属性一样的使用方式，既支持默认值，也支持类型校验，同时还保证了数据的并发安全，非常简单且强大。</p> 
<pre><code class="language-go">type DynamicConfig struct &#123;
Int   dync.Int64   `value:"$&#123;int:=3&#125;" validate:"$<6"`
Float dync.Float64 `value:"$&#123;float:=1.2&#125;"`
Map   dync.Ref     `value:"$&#123;map:=&#125;"`
Slice dync.Ref     `value:"$&#123;slice:=&#125;"`
Event dync.Event   `value:"$&#123;event&#125;"`
&#125;

type DynamicConfigWrapper struct &#123;
Wrapper DynamicConfig `value:"$&#123;wrapper&#125;"`
&#125;

func TestDynamic(t *testing.T) &#123;

var cfg *DynamicConfig
wrapper := new(DynamicConfigWrapper)

c := gs.New()
c.Provide(func() *DynamicConfig &#123;
config := new(DynamicConfig)
config.Int.OnValidate(func(v int64) error &#123;
if v < 3 &#123;
return errors.New("should greeter than 3")
&#125;
return nil
&#125;)
config.Slice.Init(make([]string, 0))
config.Map.Init(make(map[string]string))
config.Event.OnEvent(func(prop *conf.Properties) error &#123;
fmt.Println("event fired.")
return nil
&#125;)
return config
&#125;).Init(func(config *DynamicConfig) &#123;
cfg = config
&#125;)
c.Object(wrapper).Init(func(p *DynamicConfigWrapper) &#123;
p.Wrapper.Slice.Init(make([]string, 0))
p.Wrapper.Map.Init(make(map[string]string))
p.Wrapper.Event.OnEvent(func(prop *conf.Properties) error &#123;
fmt.Println("event fired.")
return nil
&#125;)
&#125;)
err := c.Refresh()
assert.Nil(t, err)

&#123;
b, _ := json.Marshal(cfg)
assert.Equal(t, string(b), `&#123;"Int":3,"Float":1.2,"Map":&#123;&#125;,"Slice":[],"Event":&#123;&#125;&#125;`)
b, _ = json.Marshal(wrapper)
assert.Equal(t, string(b), `&#123;"Wrapper":&#123;"Int":3,"Float":1.2,"Map":&#123;&#125;,"Slice":[],"Event":&#123;&#125;&#125;&#125;`)
&#125;

&#123;
p := conf.New()
p.Set("int", 4)
p.Set("float", 2.3)
p.Set("map.a", 1)
p.Set("map.b", 2)
p.Set("slice[0]", 3)
p.Set("slice[1]", 4)
p.Set("wrapper.int", 3)
p.Set("wrapper.float", 1.5)
p.Set("wrapper.map.a", 9)
p.Set("wrapper.map.b", 8)
p.Set("wrapper.slice[0]", 4)
p.Set("wrapper.slice[1]", 6)
c.Properties().Refresh(p)
&#125;

&#123;
b, _ := json.Marshal(cfg)
assert.Equal(t, string(b), `&#123;"Int":4,"Float":2.3,"Map":&#123;"a":"1","b":"2"&#125;,"Slice":["3","4"],"Event":&#123;&#125;&#125;`)
b, _ = json.Marshal(wrapper)
assert.Equal(t, string(b), `&#123;"Wrapper":&#123;"Int":3,"Float":1.5,"Map":&#123;"a":"9","b":"8"&#125;,"Slice":["4","6"],"Event":&#123;&#125;&#125;&#125;`)
&#125;
&#125;</code></pre> 
<p><strong>Bean 共享</strong></p> 
<p>Java Spring Redis 在首页使用了一个非常特别的特性，可以将一个 Bean 的字段值注入到另一个对象中，看起来就像是 Bean 被共享了。现在 Go-Spring 也能支持这样的使用方式。</p> 
<pre><code class="language-go">type runner struct &#123;
Client *redis.Client           `autowire:""`
StrOps *redis.StringOperations `autowire:"RedisClient"`
&#125;

func (r *runner) Run(ctx gs.Context) &#123;

_, err := r.Client.OpsForString().Get(ctx.Context(), "nonexisting")
if !redis.IsErrNil(err) &#123;
panic(errors.New("should be redis.ErrNil"))
&#125;

_, err = r.Client.OpsForString().Set(ctx.Context(), "mykey", "Hello")
util.Panic(err).When(err != nil)

v, err := r.Client.OpsForString().Get(ctx.Context(), "mykey")
util.Panic(err).When(err != nil)

if v != "Hello" &#123;
panic(errors.New("should be \"Hello\""))
&#125;

v, err = r.StrOps.Get(ctx.Context(), "mykey")
util.Panic(err).When(err != nil)

if v != "Hello" &#123;
panic(errors.New("should be \"Hello\""))
&#125;

go gs.ShutDown()
&#125;

func main() &#123;
gs.Object(&runner&#123;&#125;).Export((*gs.AppRunner)(nil))
fmt.Printf("program exited %v\n", gs.Web(false).Run())
&#125;</code></pre>
                                        </div>
                                      
</div>
            