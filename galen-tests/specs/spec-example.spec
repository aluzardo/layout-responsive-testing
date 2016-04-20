@objects
   header          css    #header
   menu            css    #menu
   content         css    #content-container
   side-panel      css    #side-panel
   footer          css    #footer
   
= Header =
    header:
      @on desktop 
          visible
      @on tablet 
          visible
      @on mobile 
          visible

= Menu =
    menu:
      @on desktop 
          visible
      @on tablet 
          visible
      @on mobile 
          visible

= Content =
    content:
      @on desktop 
          visible
      @on tablet 
          visible
      @on mobile 
          visible

= Side Panel =
    side-panel:
      @on desktop 
          width 300px
      @on tablet 
          width 300px
      @on mobile 
          width 100 % of screen/width

= Footer =
    footer:
      @on desktop 
          visible
      @on tablet 
          visible
      @on mobile 
          visible