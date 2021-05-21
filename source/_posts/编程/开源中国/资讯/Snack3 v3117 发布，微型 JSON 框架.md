
---
title: 'Snack3 v3.1.17 发布，微型 JSON 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9933'
author: 开源中国
comments: false
date: Fri, 21 May 2021 11:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9933'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Snack3 v3.1.17 已经发布，此版本更新内容包括：</p> 
<ul> 
 <li>完全改造为基于 无参构函数 和 字段的操作，避免因数据注入而诱发恶意动作。</li> 
</ul> 
<h1>Snack3 for java</h1> 
<p>一个微型JSON + Jsonpath框架</p> 
<p>基于jdk8，70kb。支持：序列化反序列化、解析和转换、Json path 查询。</p> 
<pre><dependency>
  <groupId>org.noear</groupId>
  <artifactId>snack3</artifactId>
  <version>3.1.17</version>
</dependency></pre> 
<p>Snack3 借鉴了 <code>Javascript</code> 所有变量由 <code>var</code> 申明，及 <code>Xml dom</code> 一切都是 <code>Node</code> 的设计。其下一切数据都以<code>ONode</code>表示，<code>ONode</code>也即 <code>One node</code> 之意，代表任何类型，也可以转换为任何类型。</p> 
<ul> 
 <li>强调文档树的操控和构建能力</li> 
 <li>做为中间媒体，方便不同格式互转</li> 
 <li>高性能<code>Json path</code>查询（兼容性和性能很赞）</li> 
 <li>支持<code>序列化、反序列化</code></li> 
 <li>基于 无参构造函数 + 字段 操作实现（因注入而触发动作的风险，不会有）</li> 
</ul> 
<h2>随便放几个示例</h2> 
<pre>//demo0::字符串化
String json = ONode.stringify(user); 

//demo1::序列化
// -- 输出带@type
String json = ONode.serialize(user); 

//demo2::反序列化
// -- json 有已带@type
UserModel user = ONode.deserialize(json); 
// -- json 可以不带@type (clz 申明了)
UserModel user = ONode.deserialize(json, UserModel.class); 
// -- json 可以不带@type，泛型方式输出（类型是已知的）
List<UserModel> list = ONode.deserialize(json, (new ArrayList<UserModel>()&#123;&#125;).getClass()); 

//demo3::转为ONode
ONode o = ONode.loadStr(json); //将json String 转为 ONode
ONode o = ONode.loadObj(user); //将java Object 转为 ONode

//demo3.1::转为ONode，取子节点进行序列化
ONode o = ONode.loadStr(json);
UserModel user = o.get("user").toObject(UserModel.class);


//demo4:构建json数据(极光推送的rest api调用)
public static void push(Collection<String> alias_ary, String text)  &#123;
    ONode data = new ONode().build((d)->&#123;
        d.getOrNew("platform").val("all");

        d.getOrNew("audience").getOrNew("alias").addAll(alias_ary);

        d.getOrNew("options")
                .set("apns_production",false);

        d.getOrNew("notification").build(n->&#123;
            n.getOrNew("ios")
                    .set("alert",text)
                    .set("badge",0)
                    .set("sound","happy");
        &#125;);
    &#125;);

    String message = data.toJson();
    String author = Base64Util.encode(appKey+":"+masterSecret);

    Map<String,String> headers = new HashMap<>();
    headers.put("Content-Type","application/json");
    headers.put("Authorization","Basic "+author);

    HttpUtil.postString(apiUrl, message, headers);
&#125;

//demo5:取值
o.get("name").getString();
o.get("num").getInt();
o.get("list").get(0).get("lev").getInt();

//demo5.1::取值并转换
UserModel user = o.get("user").toObject(UserModel.class); //取user节点，并转为UserModel

//demo5.2::取值并填充
o.get("list2").fill("[1,2,3,4,5,5,6]");


//demo6::json path //不确定返回数量的，者会返回array类型
//找到所有的187开头的手机号，改为186，最后输出修改后的json
o.select("$..mobile[?(@ =~ /^187/)]").forEach(n->n.val("186")).toJson();
//找到data.list[1]下的的mobile字段，并转为long
o.select("$.data.list[1].mobile").getLong();

//查找所有手机号，并转为List<String> 
List<String> list = o.select("$..mobile").toObject(List.class);
//查询data.list下的所有mobile，并转为List<String>
List<String> list = o.select("$.data.list[*].mobile").toObject(List.class);
//找到187手机号的用户，并输出List<UserModel>
List<UserModel> list = o.select("$.data.list[?(@.mobile =~ /^187/)]")
                        .toObjectList(UserModel.class);
//或
List<UserModel> list = o.select("$.data.list[?(@.mobile =~ /^187/)]")
                        .toObjectList(UserModel.class);


//demo7:遍历
//如果是个Object
o.forEach((k,v)->&#123;
  //...
&#125;);
//如果是个Array
o.forEach((v)->&#123;
  //...
&#125;);

//demo8:互转
String xml = "<xml>....</xml>";
XmlFromer xmlFromer = new XmlFromer();
YmalToer  ymalToer  = new YmalToer();

//加载xml，输出ymal
String ymal = ONode.load(xml,Constants.def(),xmlFromer).to(ymalToer);

//加载xml，去掉手机号，再转为java object
ONode tmp =ONode.load(xml,Constants.def(),xmlFromer);
tmp.select("$..[?(@.mobile)]").forEach(n->n.remove("mobile"));
XxxModel m =tmp.toObject(XxxModel.class);
</pre> 
<p>详情查看：<a href="https://gitee.com/noear/snack3/releases/v3.1.17">https://gitee.com/noear/snack3/releases/v3.1.17</a></p>
                                        </div>
                                      
</div>
            