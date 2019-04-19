#通配符选择器  *[:为状态]空格{}       改变所有控件的样式
#类型选择器  类名[:为状态]空格{}      改变这个类的对象和继承自这个类的所有的对象的样式
#id选择器    #id[:为状态]空格{}
#属性选择器  [属性名='属性值'][:为状态]空格{}
#后代选择器  父控件#id空格子控件    包含直接包含和间接包含
#子选择器    父控件#id>子控件        只是直接包含
#子控件选择器   指的是复合控件控件，比如CheckBox  #控件id::indicator:checked {image:url('1.jpg');}
                                                  #控件id::indicator {width:20px;height:20px}
                                                 #控件id::indicator:unchecked {image:url('001_01.png');}
QCheckBox,QRidioButton  ::indicator
QComboBox   ::drop-down
QSpinBox,QDateEdit,QTimeEdit,QDateTimeEdit  ::up-button  ::down-button ::op-arrow  ::down-arrow