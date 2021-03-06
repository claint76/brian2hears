.. note::
    :class: sphx-glr-download-link-note

    Click :ref:`here <sphx_glr_download_auto_examples_log_gammachirp.py>` to download the full example code
.. rst-class:: sphx-glr-example-title

.. _sphx_glr_auto_examples_log_gammachirp.py:


Logarithmic Gammachirp filters
------------------------------
Example of the use of the class :class:`~brian2hears.LogGammachirp` available in
the library. It implements a filterbank of IIR gammachirp filters as 
Unoki et al. 2001, "Improvement of an IIR asymmetric compensation gammachirp
filter". In this example, a white noise is filtered by a linear gammachirp
filterbank and the resulting cochleogram is plotted. The different impulse
responses are also plotted.



.. image:: /auto_examples/images/sphx_glr_log_gammachirp_001.png
    :class: sphx-glr-single-img





.. code-block:: default

    from brian2 import *
    from brian2hears import *

    sound = whitenoise(100*ms).ramp()
    sound.level = 50*dB

    nbr_center_frequencies = 50  #number of frequency channels in the filterbank

    c1 = -2.96 #glide slope
    b1 = 1.81  #factor determining the time constant of the filters

    #center frequencies with a spacing following an ERB scale
    cf = erbspace(100*Hz, 1000*Hz, nbr_center_frequencies)

    gamma_chirp = LogGammachirp(sound, cf, c=c1, b=b1) 

    gamma_chirp_mon = gamma_chirp.process()

    figure()
    imshow(flipud(gamma_chirp_mon.T), aspect='auto')    
    show()    


.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  0.180 seconds)


.. _sphx_glr_download_auto_examples_log_gammachirp.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download

     :download:`Download Python source code: log_gammachirp.py <log_gammachirp.py>`



  .. container:: sphx-glr-download

     :download:`Download Jupyter notebook: log_gammachirp.ipynb <log_gammachirp.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.readthedocs.io>`_
