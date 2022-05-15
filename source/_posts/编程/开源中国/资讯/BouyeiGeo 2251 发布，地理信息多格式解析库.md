
---
title: 'Bouyei.Geo 22.5.1 发布，地理信息多格式解析库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4234'
author: 开源中国
comments: false
date: Sun, 15 May 2022 14:16:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4234'
---

<div>   
<div class="content">
                                                                    
                                                        <p>更新版本22.5.1：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FBouyei.Geo" target="_blank">https://www.nuget.org/packages/Bouyei.Geo</a></p> 
<ul> 
 <li>优化mdb,gdb,wkt,wkb等文件解析和反解析。</li> 
 <li>增加postgis的原生byte[]打包写入到数据库。</li> 
 <li>优化multipolygon的图形椭球面积计算。</li> 
</ul> 
<pre><code>   static void TestWkbFromPg()
        &#123;
            string connstr = "Server=127.0.0.1;Port=5432;User Id=postgres;Password=123456;Database=db;";
            using (IAdoProvider provider = AdoProvider.CreateProvider(connstr, FactoryType.PostgreSQL))
            &#123;
                var param = new Parameter("select cjdm,cjmc,ST_AsEWKB(geom) as ewkb from cn_xzq");
                var tb = provider.Query(param);

                var rt = provider.Query<cn_xzq>(param);
                if (rt.IsSuccess() == false)
                    throw new Exception(rt.Info);

                var items = rt.Result;
                foreach(var item in items)
                &#123; 
                    PostGISParser parser = new PostGISParser();
                    var geo= parser.FromReader(item.ewkb);
                     var arry=parser.ToWriter(geo);



                    //验证解析和反解析是否一致

                    for(int i = 0; i < item.ewkb.Length;++i)
                    &#123;
                        if (item.ewkb[i] != arry[i])
                        &#123;
                            throw new Exception(i.ToString()+"不匹配");
                        &#125;
                    &#125;
                &#125;
            &#125;
        &#125;

        static void TestFromEsriMdb()
        &#123;
            string connstr = @"Provider=Microsoft.ACE.OLEDB.12.0;Data Source=F:\\g.mdb;";
            using (IAdoProvider provider = AdoProvider.CreateProvider(connstr, FactoryType.OleDb))
            &#123;
                var rt = provider.Query<Item>(new Parameter("select top 1 SHAPE as wkb from mpoint"));
                var items = rt.Result;
                List<Geometry> geos = new List<Geometry>();
                foreach (var item in items)
                &#123;
                    EsriMdbParser wkbParser = new EsriMdbParser();
                    //解析和反解析字节
                    var geo = wkbParser.FromReader(item.wkb);
                    var buf = wkbParser.ToWriter(geo);
                    var ngeo = wkbParser.FromReader(buf);

                    //生成wkt
                    string wkt = geo.ToWkt();

                    geos.Add(geo);
                &#125;
            &#125;
        &#125;</code></pre> 
<p> </p>
                                        </div>
                                      
</div>
            